# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--14_18:22:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **45,570 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 18:22:28 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:12:42 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.009 |  |
| 2026-01-14 18:11:04 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-01-14 18:08:02 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:07:33 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:07:11 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:07:00 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:06:39 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.009 |  |
| 2026-01-14 18:06:23 | Panadugama (Nilwala Ganga) | 3.34 | 🟢 Normal | 1.120 | 🔺 Rising |
| 2026-01-14 18:05:39 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-01-14 18:05:15 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:05:05 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-01-14 18:04:29 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.020 |  |
| 2026-01-14 18:04:20 | Hanwella (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-14 18:04:14 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.005 |  |
| 2026-01-14 18:03:40 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:03:38 | Manampitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.021 |  |
| 2026-01-14 18:03:35 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:03:33 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-14 18:03:03 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:02:52 | Thanthirimale (Malwathu Oya) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-01-14 18:02:43 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:02:42 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-01-14 18:02:31 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-14 18:02:25 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:02:18 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-01-14 18:02:16 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-01-14 18:02:08 | Horowpothana (Yan Oya) | 2.96 | 🟢 Normal | -0.024 |  |
| 2026-01-14 18:01:49 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-14 18:01:39 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.030 |  |
| 2026-01-14 18:01:30 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:01:24 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:01:23 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-14 18:01:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-01-14 18:01:08 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-14 18:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:00:28 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.031 |  |
| 2026-01-14 18:00:19 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:00:11 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 18:06:23 | Panadugama (Nilwala Ganga) | 3.34 | 🟢 Normal | 1.120 | 🔺 Rising |
| 2026-01-14 18:02:16 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-01-14 18:05:05 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-01-14 18:01:08 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-14 18:02:31 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-14 18:01:23 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-14 18:01:49 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-14 18:03:33 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-14 18:04:14 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.005 |  |
| 2026-01-14 18:00:19 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:03:40 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:00:11 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:03:35 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:02:43 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:01:24 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:07:11 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:08:02 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:02:25 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:22:28 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:03:03 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:07:00 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:01:30 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:07:33 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:12:42 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.009 |  |
| 2026-01-14 18:06:39 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.009 |  |
| 2026-01-14 18:04:20 | Hanwella (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-14 18:05:39 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-01-14 18:01:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-01-14 17:02:21 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.010 |  |
| 2026-01-14 18:02:18 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-01-14 18:02:42 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-01-14 18:04:29 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.020 |  |
| 2026-01-14 18:02:52 | Thanthirimale (Malwathu Oya) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-01-14 18:03:38 | Manampitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.021 |  |
| 2026-01-14 18:02:08 | Horowpothana (Yan Oya) | 2.96 | 🟢 Normal | -0.024 |  |
| 2026-01-14 18:01:39 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.030 |  |
| 2026-01-14 18:11:04 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-01-14 18:00:28 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.031 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)