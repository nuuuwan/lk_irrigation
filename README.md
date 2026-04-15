# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_14:19:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **125,791 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 14:19:48 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-15 14:15:11 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:15:01 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:15:00 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:13:42 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.019 |  |
| 2026-04-15 14:11:27 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.009 |  |
| 2026-04-15 14:10:35 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:09:25 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.059 |  |
| 2026-04-15 14:07:17 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:07:17 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-15 14:07:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | -0.029 |  |
| 2026-04-15 14:07:10 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.018 |  |
| 2026-04-15 14:07:07 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-04-15 14:05:50 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.039 |  |
| 2026-04-15 14:05:45 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.024 |  |
| 2026-04-15 14:05:00 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:04:54 | Peradeniya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-04-15 14:04:38 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:04:33 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:04:16 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:04:15 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-04-15 14:04:02 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:03:55 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:03:32 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:03:29 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:03:28 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-15 14:03:23 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:02:58 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:02:29 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-04-15 14:02:28 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.050 |  |
| 2026-04-15 14:02:27 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:02:12 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:02:08 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | -0.011 |  |
| 2026-04-15 14:02:00 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:01:43 | Thanthirimale (Malwathu Oya) | 2.56 | 🟢 Normal | -0.030 |  |
| 2026-04-15 14:01:34 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:01:19 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-04-15 14:01:06 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:00:51 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:00:42 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:00:18 | Weraganthota (Mahaweli Ganga) | -2.81 | 🟢 Normal | -0.061 |  |
| 2026-04-15 13:51:49 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.064 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 14:01:19 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-04-15 14:19:48 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-15 13:07:24 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-15 14:03:28 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-15 14:03:55 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:00:51 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:02:27 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:02:00 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:04:33 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:02:58 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:01:06 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:04:38 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:10:35 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:03:32 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:15:11 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:04:16 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:02:12 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:04:02 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:03:29 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:00:42 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:01:34 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:03:23 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:07:17 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:11:27 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.009 |  |
| 2026-04-15 14:02:29 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-04-15 14:04:15 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-04-15 14:07:17 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-15 14:04:54 | Peradeniya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-04-15 14:02:08 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | -0.011 |  |
| 2026-04-15 14:07:10 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.018 |  |
| 2026-04-15 14:13:42 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.019 |  |
| 2026-04-15 14:07:07 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-04-15 14:05:45 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.024 |  |
| 2026-04-15 14:07:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | -0.029 |  |
| 2026-04-15 14:01:43 | Thanthirimale (Malwathu Oya) | 2.56 | 🟢 Normal | -0.030 |  |
| 2026-04-15 14:05:50 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.039 |  |
| 2026-04-15 14:02:28 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.050 |  |
| 2026-04-15 14:09:25 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.059 |  |
| 2026-04-15 14:00:18 | Weraganthota (Mahaweli Ganga) | -2.81 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)