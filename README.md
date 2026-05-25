# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--25_22:09:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **161,614 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 22:09:33 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-25 22:09:25 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:09:15 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.019 |  |
| 2026-05-25 22:07:24 | Putupaula (Kalu Ganga) | 2.72 | 🟢 Normal | -0.037 |  |
| 2026-05-25 22:06:43 | Ellagawa (Kalu Ganga) | 8.70 | 🟢 Normal | -0.049 |  |
| 2026-05-25 22:06:20 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:05:50 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | -0.009 |  |
| 2026-05-25 22:05:27 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-05-25 22:05:19 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | -0.010 |  |
| 2026-05-25 22:05:19 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-05-25 22:04:31 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-25 22:04:27 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:03:55 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-25 22:03:50 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:03:43 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-25 22:03:21 | Glencourse (Kelani Ganga) | 11.38 | 🟢 Normal | -0.020 |  |
| 2026-05-25 22:02:45 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-25 22:02:45 | Hanwella (Kelani Ganga) | 4.03 | 🟢 Normal | -0.059 |  |
| 2026-05-25 22:02:33 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:02:11 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:02:00 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:02:00 | Deraniyagala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 22:01:57 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:01:57 | Rathnapura (Kalu Ganga) | 4.00 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-25 22:01:37 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.069 |  |
| 2026-05-25 22:01:27 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:01:21 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:01:18 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:01:16 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:01:12 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:01:06 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:00:39 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:00:17 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 20:01:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | -0.061 |  |
| 2026-05-25 22:05:19 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-05-25 22:04:31 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-25 22:01:57 | Rathnapura (Kalu Ganga) | 4.00 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-25 22:03:43 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-25 22:09:33 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-25 22:02:45 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-25 22:03:55 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-25 22:02:00 | Deraniyagala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 22:01:18 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:02:11 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:01:21 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:00:39 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:01:57 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:09:25 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:02:33 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:04:27 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:00:17 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:01:06 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:02:00 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:03:50 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:06:20 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-25 21:15:28 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:01:27 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:01:12 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:01:16 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 22:05:50 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | -0.009 |  |
| 2026-05-25 21:04:06 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-25 18:01:32 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-05-25 22:05:27 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-05-25 22:05:19 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | -0.010 |  |
| 2026-05-25 18:02:07 | Galgamuwa (Mee Oya) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-05-25 22:09:15 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.019 |  |
| 2026-05-25 22:03:21 | Glencourse (Kelani Ganga) | 11.38 | 🟢 Normal | -0.020 |  |
| 2026-05-25 18:01:42 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-05-25 22:07:24 | Putupaula (Kalu Ganga) | 2.72 | 🟢 Normal | -0.037 |  |
| 2026-05-25 22:06:43 | Ellagawa (Kalu Ganga) | 8.70 | 🟢 Normal | -0.049 |  |
| 2026-05-25 22:02:45 | Hanwella (Kelani Ganga) | 4.03 | 🟢 Normal | -0.059 |  |
| 2026-05-25 22:01:37 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)