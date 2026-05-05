# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--05_10:14:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **143,431 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 10:14:23 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:12:35 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:12:27 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:11:25 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-05 10:09:55 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | -0.018 |  |
| 2026-05-05 10:08:53 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.028 |  |
| 2026-05-05 10:08:10 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.009 |  |
| 2026-05-05 10:07:27 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.045 |  |
| 2026-05-05 10:07:15 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:06:03 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:05:49 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.019 |  |
| 2026-05-05 10:05:45 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:05:31 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:05:20 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:05:12 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-05 10:04:49 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:04:40 | Glencourse (Kelani Ganga) | 9.53 | 🟢 Normal | -0.093 |  |
| 2026-05-05 10:04:27 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:04:14 | Thalgahagoda (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.041 |  |
| 2026-05-05 10:04:07 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:03:58 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:03:45 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.069 |  |
| 2026-05-05 10:03:12 | Hanwella (Kelani Ganga) | 1.46 | 🟢 Normal | -0.040 |  |
| 2026-05-05 10:03:08 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-05 10:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:02:33 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-05-05 10:02:26 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.005 |  |
| 2026-05-05 10:02:14 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.175 |  |
| 2026-05-05 10:01:55 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:01:53 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:01:51 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:01:49 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-05-05 10:01:42 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-05-05 10:01:15 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.086 |  |
| 2026-05-05 10:01:08 | Ellagawa (Kalu Ganga) | 4.86 | 🟢 Normal | -0.021 |  |
| 2026-05-05 10:01:07 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:00:56 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:00:47 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.010 |  |
| 2026-05-05 10:00:26 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 10:05:12 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-05 10:11:25 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-05 10:03:08 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-05 10:01:07 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:01:53 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:03:58 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:12:27 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:00:56 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:05:20 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:14:23 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:12:35 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:01:51 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:04:07 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:04:49 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:07:15 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:05:31 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:04:27 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:00:26 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:06:03 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:05:45 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:01:55 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-05-05 10:02:26 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.005 |  |
| 2026-05-05 10:08:10 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.009 |  |
| 2026-05-05 10:01:49 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-05-05 10:01:42 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-05-05 10:00:47 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.010 |  |
| 2026-05-05 10:09:55 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | -0.018 |  |
| 2026-05-05 10:05:49 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.019 |  |
| 2026-05-05 10:02:33 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-05-05 10:01:08 | Ellagawa (Kalu Ganga) | 4.86 | 🟢 Normal | -0.021 |  |
| 2026-05-05 10:08:53 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.028 |  |
| 2026-05-05 10:03:12 | Hanwella (Kelani Ganga) | 1.46 | 🟢 Normal | -0.040 |  |
| 2026-05-05 10:04:14 | Thalgahagoda (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.041 |  |
| 2026-05-05 10:07:27 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.045 |  |
| 2026-05-05 10:03:45 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.069 |  |
| 2026-05-05 10:01:15 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.086 |  |
| 2026-05-05 10:04:40 | Glencourse (Kelani Ganga) | 9.53 | 🟢 Normal | -0.093 |  |
| 2026-05-05 10:02:14 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.175 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)