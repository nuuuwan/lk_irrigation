# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--24_16:10:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **188,221 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 16:10:50 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | -0.018 |  |
| 2026-06-24 16:09:09 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | -0.010 |  |
| 2026-06-24 16:08:58 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.009 |  |
| 2026-06-24 16:08:50 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.046 |  |
| 2026-06-24 16:08:19 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:08:09 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:07:25 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.037 |  |
| 2026-06-24 16:06:04 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:05:48 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -0.020 |  |
| 2026-06-24 16:05:32 | Dunamale (Aththanagalu Oya) | 2.72 | 🟢 Normal | -0.020 |  |
| 2026-06-24 16:04:28 | Putupaula (Kalu Ganga) | 1.81 | 🟢 Normal | -0.089 |  |
| 2026-06-24 16:04:23 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:03:44 | Glencourse (Kelani Ganga) | 10.48 | 🟢 Normal | -0.080 |  |
| 2026-06-24 16:03:39 | Hanwella (Kelani Ganga) | 2.62 | 🟢 Normal | -0.020 |  |
| 2026-06-24 16:03:34 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:03:18 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:03:13 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-06-24 16:03:12 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.019 |  |
| 2026-06-24 16:03:09 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:03:06 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:02:54 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-06-24 16:02:39 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.040 |  |
| 2026-06-24 16:02:35 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:02:19 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:02:16 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 16:02:06 | Ellagawa (Kalu Ganga) | 6.09 | 🟢 Normal | -0.117 |  |
| 2026-06-24 16:02:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.90 | 🟢 Normal | -0.081 |  |
| 2026-06-24 16:02:00 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.031 |  |
| 2026-06-24 16:01:57 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:01:53 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-06-24 16:01:41 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:01:37 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | -0.011 |  |
| 2026-06-24 16:01:33 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.012 |  |
| 2026-06-24 16:01:09 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:00:45 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:00:42 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-24 16:00:25 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:00:19 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 16:03:13 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-06-24 16:02:16 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 16:00:25 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:01:41 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:03:06 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:06:04 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:01:09 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:01:57 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:08:09 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:02:35 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:03:18 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:03:09 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:04:23 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:08:19 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:03:34 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:02:19 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:00:45 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:00:19 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 16:08:58 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.009 |  |
| 2026-06-24 16:00:42 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-24 16:09:09 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | -0.010 |  |
| 2026-06-24 16:01:53 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-06-24 15:08:53 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-06-24 16:01:37 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | -0.011 |  |
| 2026-06-24 16:01:33 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.012 |  |
| 2026-06-24 16:10:50 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | -0.018 |  |
| 2026-06-24 16:03:12 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.019 |  |
| 2026-06-24 16:05:48 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -0.020 |  |
| 2026-06-24 16:05:32 | Dunamale (Aththanagalu Oya) | 2.72 | 🟢 Normal | -0.020 |  |
| 2026-06-24 16:03:39 | Hanwella (Kelani Ganga) | 2.62 | 🟢 Normal | -0.020 |  |
| 2026-06-24 16:02:54 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-06-24 16:02:00 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.031 |  |
| 2026-06-24 16:07:25 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.037 |  |
| 2026-06-24 16:02:39 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.040 |  |
| 2026-06-24 16:08:50 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.046 |  |
| 2026-06-24 16:03:44 | Glencourse (Kelani Ganga) | 10.48 | 🟢 Normal | -0.080 |  |
| 2026-06-24 16:02:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.90 | 🟢 Normal | -0.081 |  |
| 2026-06-24 16:04:28 | Putupaula (Kalu Ganga) | 1.81 | 🟢 Normal | -0.089 |  |
| 2026-06-24 16:02:06 | Ellagawa (Kalu Ganga) | 6.09 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)