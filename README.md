# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_05:20:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **135,258 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 05:20:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-26 05:16:56 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -2.439 |  |
| 2026-04-26 05:15:52 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | -0.196 |  |
| 2026-04-26 05:14:36 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:12:09 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-04-26 05:10:05 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:10:03 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:10:00 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:09:57 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:09:45 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | -0.196 |  |
| 2026-04-26 05:08:34 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.028 |  |
| 2026-04-26 05:06:48 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.091 |  |
| 2026-04-26 05:06:09 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.358 |  |
| 2026-04-26 05:06:03 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.019 |  |
| 2026-04-26 05:05:29 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:04:46 | Glencourse (Kelani Ganga) | 8.97 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:04:19 | Glencourse (Kelani Ganga) | 8.97 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:04:15 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:03:39 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -2.439 |  |
| 2026-04-26 05:03:20 | Moragaswewa (Deduru Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-04-26 05:03:11 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.011 |  |
| 2026-04-26 05:03:09 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-04-26 05:03:03 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:03:01 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:03:01 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-26 05:02:48 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:02:42 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.039 |  |
| 2026-04-26 05:02:36 | Katharagama (Menik Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:02:35 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.013 |  |
| 2026-04-26 05:02:07 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:01:47 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:01:47 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:01:31 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-04-26 05:01:28 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:01:22 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.040 |  |
| 2026-04-26 05:01:08 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:58:14 | Panadugama (Nilwala Ganga) | 3.38 | 🟢 Normal | -0.196 |  |
| 2026-04-26 04:40:19 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.091 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 05:03:01 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-26 05:20:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-26 04:01:37 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-26 05:02:48 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:01:28 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:01:47 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:03:01 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:14:36 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:03:34 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:04:15 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:05:29 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:10:05 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:04:46 | Glencourse (Kelani Ganga) | 8.97 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:03:03 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:01:47 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:02:36 | Katharagama (Menik Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:01:08 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:06:00 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-26 04:05:50 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:02:07 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-26 05:12:09 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-04-26 05:03:20 | Moragaswewa (Deduru Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-04-26 04:00:31 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-04-26 05:03:09 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-04-26 04:02:52 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-04-26 05:03:11 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.011 |  |
| 2026-04-26 05:02:35 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.013 |  |
| 2026-04-26 05:06:03 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.019 |  |
| 2026-04-25 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.020 |  |
| 2026-04-26 05:01:31 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-04-25 18:01:09 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-04-26 05:08:34 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.028 |  |
| 2026-04-26 05:02:42 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.039 |  |
| 2026-04-26 05:01:22 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.040 |  |
| 2026-04-25 18:00:50 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.050 |  |
| 2026-04-26 05:06:48 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.091 |  |
| 2026-04-26 05:15:52 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | -0.196 |  |
| 2026-04-26 05:06:09 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.358 |  |
| 2026-04-26 05:16:56 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -2.439 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)