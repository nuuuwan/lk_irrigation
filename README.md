# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--15_05:33:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **45,947 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 05:33:44 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:18:20 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:18:18 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:17:48 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | -0.837 |  |
| 2026-01-15 05:14:56 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-15 05:08:59 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-15 05:07:16 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:06:42 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:06:32 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:06:31 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:06:26 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:06:21 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:05:49 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:04:42 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | -0.047 |  |
| 2026-01-15 05:04:26 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-15 05:04:22 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-01-15 05:04:14 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.061 |  |
| 2026-01-15 05:04:13 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | -0.029 |  |
| 2026-01-15 05:04:08 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:03:53 | Horowpothana (Yan Oya) | 2.47 | 🟢 Normal | -0.031 |  |
| 2026-01-15 05:03:45 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:03:12 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:03:04 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:02:05 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:01:55 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.153 |  |
| 2026-01-15 05:01:47 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-01-15 05:01:30 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.039 |  |
| 2026-01-15 05:01:30 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:01:23 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.031 |  |
| 2026-01-15 05:01:16 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | -0.010 |  |
| 2026-01-15 05:01:10 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-15 05:00:51 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-01-15 05:00:48 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.064 |  |
| 2026-01-15 05:00:40 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-15 05:00:21 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 03:04:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-15 05:14:56 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-15 05:00:40 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-15 05:04:26 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-15 05:08:59 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-15 05:00:21 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 03:18:27 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-15 05:03:04 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:00:19 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:05:49 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:33:44 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:03:12 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:04:08 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:02:43 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:18:20 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:07:16 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:06:32 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:06:31 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:06:21 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-15 04:14:28 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:02:05 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:03:45 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:01:30 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:06:42 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-15 05:01:16 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | -0.010 |  |
| 2026-01-15 05:00:51 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-01-15 05:01:47 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-01-15 05:01:10 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-14 18:02:52 | Thanthirimale (Malwathu Oya) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-01-15 05:04:22 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-01-15 05:04:13 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | -0.029 |  |
| 2026-01-15 05:01:23 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.031 |  |
| 2026-01-15 05:03:53 | Horowpothana (Yan Oya) | 2.47 | 🟢 Normal | -0.031 |  |
| 2026-01-15 05:01:30 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.039 |  |
| 2026-01-15 05:04:42 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | -0.047 |  |
| 2026-01-15 05:04:14 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.061 |  |
| 2026-01-15 05:00:48 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.064 |  |
| 2026-01-15 05:01:55 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.153 |  |
| 2026-01-15 05:17:48 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | -0.837 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)