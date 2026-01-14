# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--14_10:23:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **45,255 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 10:23:12 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.008 |  |
| 2026-01-14 10:16:00 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:07:58 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.029 |  |
| 2026-01-14 10:07:15 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | -0.030 |  |
| 2026-01-14 10:07:00 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-01-14 10:06:47 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-01-14 10:05:58 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:05:56 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:05:09 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:05:07 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-14 10:04:54 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.038 |  |
| 2026-01-14 10:04:52 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:04:35 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-14 10:04:32 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:04:30 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.014 |  |
| 2026-01-14 10:04:28 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-14 10:04:27 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:04:05 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-14 10:04:04 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:03:51 | Hanwella (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-14 10:03:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | -0.049 |  |
| 2026-01-14 10:03:43 | Thanthirimale (Malwathu Oya) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-01-14 10:03:31 | Manampitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-14 10:03:22 | Horowpothana (Yan Oya) | 3.28 | 🟢 Normal | -0.048 |  |
| 2026-01-14 10:03:21 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:03:01 | Kithulgala (Kelani Ganga) | 1.38 | 🟢 Normal | -0.165 |  |
| 2026-01-14 10:03:01 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:02:29 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:02:29 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-01-14 10:02:19 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:02:10 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:02:06 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:01:40 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | -0.010 |  |
| 2026-01-14 10:01:33 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:01:30 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:01:11 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:01:06 | Weraganthota (Mahaweli Ganga) | -1.49 | 🟢 Normal | -0.005 |  |
| 2026-01-14 10:01:04 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:00:59 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 10:07:00 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-01-14 10:05:07 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-14 10:03:31 | Manampitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-14 10:04:28 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-14 10:02:19 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:00:59 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:01:04 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:05:56 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:04:52 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:03:01 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:02:06 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:16:00 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:04:27 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:05:58 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:01:33 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:01:30 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:02:29 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:05:09 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:03:21 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:04:32 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:04:04 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:01:11 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-14 10:01:06 | Weraganthota (Mahaweli Ganga) | -1.49 | 🟢 Normal | -0.005 |  |
| 2026-01-14 10:23:12 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.008 |  |
| 2026-01-14 10:06:47 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-01-14 10:04:05 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-14 10:02:29 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-01-14 10:04:35 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-14 10:01:40 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | -0.010 |  |
| 2026-01-14 10:03:51 | Hanwella (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-14 10:04:30 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.014 |  |
| 2026-01-14 10:03:43 | Thanthirimale (Malwathu Oya) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-01-14 10:07:58 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.029 |  |
| 2026-01-14 10:07:15 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | -0.030 |  |
| 2026-01-14 10:04:54 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.038 |  |
| 2026-01-14 10:03:22 | Horowpothana (Yan Oya) | 3.28 | 🟢 Normal | -0.048 |  |
| 2026-01-14 10:03:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | -0.049 |  |
| 2026-01-14 10:03:01 | Kithulgala (Kelani Ganga) | 1.38 | 🟢 Normal | -0.165 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)