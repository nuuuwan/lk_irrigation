# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--30_16:17:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **59,868 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-30 16:17:30 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.055 |  |
| 2026-01-30 16:16:33 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.016 |  |
| 2026-01-30 16:14:28 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:14:10 | Manampitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:10:15 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:09:33 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:06:33 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-30 16:06:30 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.077 |  |
| 2026-01-30 16:06:12 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-30 16:05:46 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:05:36 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:05:35 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-30 16:05:13 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.029 |  |
| 2026-01-30 16:05:13 | Thawalama (Gin Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:05:11 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:04:51 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:04:35 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-30 16:04:20 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-30 16:04:03 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-01-30 16:03:41 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-30 16:03:32 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 16:03:28 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-01-30 16:03:20 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 16:03:16 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:03:09 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:03:02 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-30 16:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-01-30 16:02:15 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:02:13 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:02:02 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:01:43 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:01:17 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:01:15 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:01:15 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-30 16:00:56 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:00:49 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:00:49 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:00:20 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:31:04 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:29:53 | Thawalama (Gin Ganga) | 0.89 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-30 16:03:41 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-30 16:06:12 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-30 16:01:15 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-30 16:03:02 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-30 16:06:33 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-30 16:04:20 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-30 16:04:35 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-30 16:03:32 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 16:03:20 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 16:05:35 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-30 16:02:02 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:00:20 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:01:43 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:03:16 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:00:49 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:04:51 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:00:49 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:10:15 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:03:09 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:01:15 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:01:17 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:02:13 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:02:15 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:09:33 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:05:46 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:14:10 | Manampitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:00:56 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:05:13 | Thawalama (Gin Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-30 15:10:33 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:05:11 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:14:28 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-30 16:03:28 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-01-30 16:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-01-30 15:02:07 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-01-30 16:04:03 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-01-30 16:16:33 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.016 |  |
| 2026-01-30 16:05:13 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.029 |  |
| 2026-01-30 16:17:30 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.055 |  |
| 2026-01-30 16:06:30 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.077 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)