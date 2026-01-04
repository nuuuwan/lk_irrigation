# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--04_17:26:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **36,591 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 17:26:11 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.015 |  |
| 2026-01-04 17:17:01 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-04 17:14:28 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.082 |  |
| 2026-01-04 17:11:36 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.028 |  |
| 2026-01-04 17:09:27 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.078 |  |
| 2026-01-04 17:08:38 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.092 |  |
| 2026-01-04 17:08:33 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.019 |  |
| 2026-01-04 17:08:15 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-04 17:07:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.63 | 🟢 Normal | -0.066 |  |
| 2026-01-04 17:06:27 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-04 17:06:21 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-04 17:05:47 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-04 17:05:27 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | -0.009 |  |
| 2026-01-04 17:05:18 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-01-04 17:04:54 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-04 17:04:53 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.019 |  |
| 2026-01-04 17:04:17 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 17:04:01 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | -0.010 |  |
| 2026-01-04 17:03:44 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-04 17:03:23 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.089 |  |
| 2026-01-04 17:03:00 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 17:02:52 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-04 17:02:45 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | -0.031 |  |
| 2026-01-04 17:02:44 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.011 |  |
| 2026-01-04 17:02:33 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-01-04 17:02:26 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-04 17:02:25 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.230 | 🔺 Rising |
| 2026-01-04 17:02:11 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-01-04 17:01:58 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-04 17:01:53 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-04 17:01:29 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-01-04 17:01:17 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-04 17:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-04 17:00:58 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-01-04 17:00:53 | Galgamuwa (Mee Oya) | 2.46 | 🟢 Normal | -0.042 |  |
| 2026-01-04 17:00:50 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-04 17:00:41 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-01-04 17:00:31 | Manampitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.020 |  |
| 2026-01-04 16:59:45 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | 0.065 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 17:02:25 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.230 | 🔺 Rising |
| 2026-01-04 16:59:45 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-01-04 17:03:44 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-04 17:05:18 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-01-04 17:03:00 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 17:04:17 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 17:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-04 17:17:01 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-04 17:05:47 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-04 17:04:54 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-04 17:01:53 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-04 17:08:15 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-04 17:06:27 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-04 17:01:58 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-04 17:02:26 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-04 17:06:21 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-04 17:05:27 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | -0.009 |  |
| 2026-01-04 17:04:01 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | -0.010 |  |
| 2026-01-04 17:02:33 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-01-04 17:02:52 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-04 17:01:29 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-01-04 17:00:50 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-04 17:01:17 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-04 17:00:41 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-01-04 17:00:58 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-01-04 17:02:11 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-01-04 17:02:44 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.011 |  |
| 2026-01-04 17:26:11 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.015 |  |
| 2026-01-04 17:04:53 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.019 |  |
| 2026-01-04 17:08:33 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.019 |  |
| 2026-01-04 17:00:31 | Manampitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.020 |  |
| 2026-01-04 17:11:36 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.028 |  |
| 2026-01-04 17:02:45 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | -0.031 |  |
| 2026-01-04 17:00:53 | Galgamuwa (Mee Oya) | 2.46 | 🟢 Normal | -0.042 |  |
| 2026-01-04 17:07:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.63 | 🟢 Normal | -0.066 |  |
| 2026-01-04 17:09:27 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.078 |  |
| 2026-01-04 17:14:28 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.082 |  |
| 2026-01-04 17:03:23 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.089 |  |
| 2026-01-04 17:08:38 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)