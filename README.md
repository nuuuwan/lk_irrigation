# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--05_03:57:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **170,755 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-05 03:57:30 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.021 |  |
| 2026-06-05 03:48:29 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-05 03:43:15 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-05 03:21:27 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-05 03:13:25 | Ellagawa (Kalu Ganga) | 6.90 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-05 03:13:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-06-05 03:09:01 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-05 03:08:49 | Magura (Kalu Ganga) | 2.12 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-05 03:08:33 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-06-05 03:06:43 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-05 03:06:24 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | 0.058 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-05 01:37:38 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | 0.430 | 🔺 Rising |
| 2026-06-05 03:13:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-06-05 03:03:01 | Nawalapitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-06-05 03:05:19 | Hanwella (Kelani Ganga) | 3.32 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-05 03:03:07 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-05 03:13:25 | Ellagawa (Kalu Ganga) | 6.90 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-05 02:09:14 | Rathnapura (Kalu Ganga) | 3.00 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-05 03:06:24 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-06-05 03:08:33 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-06-05 03:06:43 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-05 03:48:29 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-05 02:02:12 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-05 03:03:06 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-05 03:03:48 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-05 03:00:15 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-05 03:05:12 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-05 03:43:15 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-05 03:01:57 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-05 03:09:01 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-04 18:00:13 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-05 03:03:11 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-05 03:05:20 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-05 03:01:50 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-05 03:02:32 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-05 03:01:31 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 18:07:04 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-05 03:02:58 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-05 03:03:22 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-05 03:01:46 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-05 03:00:41 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-05 03:04:55 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-05 02:05:06 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-04 18:03:20 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-06-05 03:01:23 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-05 03:02:54 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-05 02:03:01 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.008 |  |
| 2026-06-05 03:03:29 | Deraniyagala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-06-05 03:57:30 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.021 |  |
| 2026-06-05 03:05:09 | Glencourse (Kelani Ganga) | 11.71 | 🟢 Normal | -0.021 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)