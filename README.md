# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_12:12:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **197,918 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 12:12:04 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:10:16 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-05 12:10:03 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:10:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.33 | 🟢 Normal | -0.022 |  |
| 2026-07-05 12:09:36 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.074 |  |
| 2026-07-05 12:08:12 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:07:48 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-05 12:07:36 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:07:28 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:07:13 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:06:46 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.014 |  |
| 2026-07-05 12:06:41 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:06:22 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:06:09 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | -0.022 |  |
| 2026-07-05 12:06:08 | Glencourse (Kelani Ganga) | 10.79 | 🟢 Normal | -0.105 |  |
| 2026-07-05 12:06:01 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:05:39 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-07-05 12:05:33 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:04:45 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | -0.032 |  |
| 2026-07-05 12:04:33 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.029 |  |
| 2026-07-05 12:04:20 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:04:12 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:03:52 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-07-05 12:03:38 | Hanwella (Kelani Ganga) | 2.95 | 🟢 Normal | -0.130 |  |
| 2026-07-05 12:03:16 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:03:03 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:02:34 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -8.182 |  |
| 2026-07-05 12:02:31 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:02:23 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:02:19 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:02:14 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-07-05 12:02:13 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | -0.049 |  |
| 2026-07-05 12:02:12 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -8.182 |  |
| 2026-07-05 12:02:08 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:01:42 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.020 |  |
| 2026-07-05 12:01:20 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:01:10 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.112 |  |
| 2026-07-05 12:00:56 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:00:40 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:00:13 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:00:13 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 12:03:52 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-07-05 12:07:48 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-05 12:10:16 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-05 12:03:03 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:06:41 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:00:40 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:02:19 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:07:28 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:02:23 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:00:56 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:02:31 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:05:33 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:04:20 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:03:16 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:12:04 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:08:12 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:07:13 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:06:22 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:00:13 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:02:08 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:07:36 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:00:13 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:10:03 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:01:20 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:04:12 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 12:02:14 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-07-05 12:06:46 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.014 |  |
| 2026-07-05 12:05:39 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-07-05 12:01:42 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.020 |  |
| 2026-07-05 12:06:09 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | -0.022 |  |
| 2026-07-05 12:10:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.33 | 🟢 Normal | -0.022 |  |
| 2026-07-05 12:04:33 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.029 |  |
| 2026-07-05 12:04:45 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | -0.032 |  |
| 2026-07-05 12:02:13 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | -0.049 |  |
| 2026-07-05 12:09:36 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.074 |  |
| 2026-07-05 12:06:08 | Glencourse (Kelani Ganga) | 10.79 | 🟢 Normal | -0.105 |  |
| 2026-07-05 12:01:10 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.112 |  |
| 2026-07-05 12:03:38 | Hanwella (Kelani Ganga) | 2.95 | 🟢 Normal | -0.130 |  |
| 2026-07-05 12:02:34 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -8.182 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)