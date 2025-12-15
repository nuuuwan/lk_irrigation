# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--15_14:27:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **18,648 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 14:27:14 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.045 |  |
| 2025-12-15 14:18:12 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:15:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | -0.044 |  |
| 2025-12-15 14:11:50 | Panadugama (Nilwala Ganga) | 3.36 | 🟢 Normal | -0.009 |  |
| 2025-12-15 14:10:47 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:09:32 | Glencourse (Kelani Ganga) | 9.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-15 14:08:04 | Rathnapura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.040 |  |
| 2025-12-15 14:08:00 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.018 |  |
| 2025-12-15 14:06:20 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:05:55 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2025-12-15 14:05:45 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:05:07 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:05:07 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.022 |  |
| 2025-12-15 14:04:55 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:04:52 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:04:38 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:03:55 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-15 14:03:42 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2025-12-15 14:03:39 | Manampitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.019 |  |
| 2025-12-15 14:03:03 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:03:01 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:02:53 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-15 14:02:47 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:02:45 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -0.040 |  |
| 2025-12-15 14:02:42 | Weraganthota (Mahaweli Ganga) | -1.32 | 🟢 Normal | -0.050 |  |
| 2025-12-15 14:02:37 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:02:35 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:02:17 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.200 |  |
| 2025-12-15 14:02:05 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:01:59 | Horowpothana (Yan Oya) | 3.93 | 🟢 Normal | -3.130 |  |
| 2025-12-15 14:01:52 | Padiyathalawa (Maduru Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-15 14:01:36 | Horowpothana (Yan Oya) | 3.95 | 🟢 Normal | -3.130 |  |
| 2025-12-15 14:01:31 | Moragaswewa (Deduru Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:01:17 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:01:15 | Horowpothana (Yan Oya) | 4.95 | 🟢 Normal | -3.130 |  |
| 2025-12-15 14:01:09 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:01:05 | Thanthirimale (Malwathu Oya) | 4.24 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:01:01 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-15 14:00:54 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:00:36 | Galgamuwa (Mee Oya) | 1.35 | 🟢 Normal | -0.112 |  |
| 2025-12-15 14:00:28 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.012 |  |
| 2025-12-15 14:00:18 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 14:05:55 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2025-12-15 14:09:32 | Glencourse (Kelani Ganga) | 9.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-15 14:02:05 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:00:18 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:01:31 | Moragaswewa (Deduru Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:10:47 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:01:17 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:04:52 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:05:45 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:04:55 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:01:09 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:03:01 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:05:07 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:02:47 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:06:20 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:04:38 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:03:03 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:01:05 | Thanthirimale (Malwathu Oya) | 4.24 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:18:12 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:02:37 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:02:35 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-15 14:11:50 | Panadugama (Nilwala Ganga) | 3.36 | 🟢 Normal | -0.009 |  |
| 2025-12-15 14:02:53 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-15 14:03:42 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2025-12-15 14:01:01 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-15 14:01:52 | Padiyathalawa (Maduru Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-15 14:03:55 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-15 14:00:28 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.012 |  |
| 2025-12-15 14:08:00 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.018 |  |
| 2025-12-15 14:03:39 | Manampitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.019 |  |
| 2025-12-15 14:05:07 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.022 |  |
| 2025-12-15 14:08:04 | Rathnapura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.040 |  |
| 2025-12-15 14:02:45 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -0.040 |  |
| 2025-12-15 14:15:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | -0.044 |  |
| 2025-12-15 14:27:14 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.045 |  |
| 2025-12-15 14:02:42 | Weraganthota (Mahaweli Ganga) | -1.32 | 🟢 Normal | -0.050 |  |
| 2025-12-15 14:00:36 | Galgamuwa (Mee Oya) | 1.35 | 🟢 Normal | -0.112 |  |
| 2025-12-15 14:02:17 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.200 |  |
| 2025-12-15 14:01:59 | Horowpothana (Yan Oya) | 3.93 | 🟢 Normal | -3.130 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)