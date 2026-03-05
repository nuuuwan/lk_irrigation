# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--05_07:00:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **89,596 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-05 07:00:49 | Manampitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.031 |  |
| 2026-03-05 07:00:45 | Thanthirimale (Malwathu Oya) | 0.92 | 🟢 Normal | -0.004 |  |
| 2026-03-05 07:00:42 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-05 07:00:27 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-03-05 07:00:08 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.105 |  |
| 2026-03-05 06:45:45 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-05 06:45:44 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-05 06:45:43 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-05 06:36:17 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-05 06:14:14 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.105 |  |
| 2026-03-05 06:12:16 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-05 06:10:32 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-05 06:07:26 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-05 06:07:07 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 06:06:49 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-05 06:06:34 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.132 |  |
| 2026-03-05 06:06:20 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-05 06:04:10 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.540 | 🔺 Rising |
| 2026-03-05 06:03:43 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-03-05 06:06:49 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-05 06:03:35 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-05 06:04:39 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-05 06:02:00 | Weraganthota (Mahaweli Ganga) | -1.70 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-03-05 06:02:17 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-05 06:07:07 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 06:02:22 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 06:06:20 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-05 06:00:53 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-05 06:01:13 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-05 06:03:04 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-05 06:45:45 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-05 06:36:17 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-05 06:02:47 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:03:35 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-05 06:05:44 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-05 06:02:48 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-03-05 06:12:16 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-05 06:03:25 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-05 06:02:32 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-05 06:02:23 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-05 06:04:58 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-05 06:02:20 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-05 06:07:26 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-05 06:10:32 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-05 07:00:42 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-05 07:00:45 | Thanthirimale (Malwathu Oya) | 0.92 | 🟢 Normal | -0.004 |  |
| 2026-03-05 06:01:49 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-03-05 07:00:27 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-03-05 06:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.028 |  |
| 2026-03-05 06:04:20 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.029 |  |
| 2026-03-05 06:01:27 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.030 |  |
| 2026-03-05 07:00:49 | Manampitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.031 |  |
| 2026-03-05 06:01:30 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.053 |  |
| 2026-03-05 06:03:25 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.058 |  |
| 2026-03-05 07:00:08 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.105 |  |
| 2026-03-05 06:06:34 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.132 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)