# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_23:38:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **117,232 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 23:38:31 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-04-05 23:26:33 | Manampitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-05 23:12:50 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-05 23:09:48 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.026 |  |
| 2026-04-05 23:07:09 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-05 23:06:34 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.009 |  |
| 2026-04-05 23:06:26 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-05 23:06:00 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | -0.009 |  |
| 2026-04-05 23:05:55 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-05 23:05:50 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-04-05 23:05:45 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-05 23:05:32 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.042 |  |
| 2026-04-05 23:05:20 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.039 |  |
| 2026-04-05 23:04:42 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.023 |  |
| 2026-04-05 23:04:21 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-04-05 23:04:18 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.035 |  |
| 2026-04-05 23:04:14 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 23:04:05 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-05 23:04:02 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.040 |  |
| 2026-04-05 23:03:08 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | -0.032 |  |
| 2026-04-05 23:02:57 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-05 23:02:52 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-04-05 23:02:47 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-05 23:02:27 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-05 23:02:25 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-05 23:02:14 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-05 23:02:09 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 23:01:51 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | -0.069 |  |
| 2026-04-05 23:01:39 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-05 23:01:30 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-04-05 23:01:15 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-05 23:01:11 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-05 23:00:43 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 23:04:21 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-04-05 23:06:26 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-05 23:26:33 | Manampitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-05 23:12:50 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-05 23:38:31 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-04-05 23:02:27 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-05 23:02:09 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 23:01:39 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-05 23:02:57 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-05 23:01:11 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-05 23:07:09 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-05 23:05:45 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-05 23:02:47 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-05 22:12:18 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 23:05:55 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-05 23:04:05 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-05 23:04:14 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 23:02:25 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-05 23:01:15 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-05 23:06:34 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.009 |  |
| 2026-04-05 23:06:00 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | -0.009 |  |
| 2026-04-05 23:02:14 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-05 23:00:43 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-04-05 23:01:30 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:02:03 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-05 23:05:50 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-04-05 23:02:52 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-04-05 23:04:42 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.023 |  |
| 2026-04-05 23:09:48 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.026 |  |
| 2026-04-05 23:03:08 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | -0.032 |  |
| 2026-04-05 23:04:18 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.035 |  |
| 2026-04-05 23:05:20 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.039 |  |
| 2026-04-05 23:04:02 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.040 |  |
| 2026-04-05 23:05:32 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.042 |  |
| 2026-04-05 18:02:13 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.050 |  |
| 2026-04-05 23:01:51 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | -0.069 |  |
| 2026-04-05 21:08:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | -0.081 |  |
| 2026-04-05 18:02:28 | Thanthirimale (Malwathu Oya) | 2.42 | 🟢 Normal | -0.088 |  |
| 2026-04-05 22:06:10 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)