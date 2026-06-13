# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--14_02:13:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **178,748 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 02:13:30 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:06:21 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:06:17 | Badalgama (Maha Oya) | 3.28 | 🟢 Normal | -0.030 |  |
| 2026-06-14 02:06:09 | Glencourse (Kelani Ganga) | 11.65 | 🟢 Normal | -0.033 |  |
| 2026-06-14 02:05:50 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:05:32 | Baddegama (Gin Ganga) | 3.09 | 🟢 Normal | -0.020 |  |
| 2026-06-14 02:05:05 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:04:35 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.029 |  |
| 2026-06-14 02:04:30 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:04:29 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:04:28 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:04:26 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:04:25 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:04:19 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | -0.040 |  |
| 2026-06-14 02:04:03 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -126.000 |  |
| 2026-06-14 02:04:01 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | -126.000 |  |
| 2026-06-14 02:03:55 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-06-14 02:03:39 | Dunamale (Aththanagalu Oya) | 3.23 | 🟢 Normal | -0.020 |  |
| 2026-06-14 02:03:24 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:03:22 | Magura (Kalu Ganga) | 3.68 | 🟢 Normal | -0.053 |  |
| 2026-06-14 02:03:03 | Hanwella (Kelani Ganga) | 3.86 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:02:30 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:02:13 | Ellagawa (Kalu Ganga) | 8.58 | 🟢 Normal | -0.021 |  |
| 2026-06-14 02:01:44 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.072 |  |
| 2026-06-14 02:01:43 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:01:25 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.030 |  |
| 2026-06-14 02:01:19 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:01:18 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.042 |  |
| 2026-06-14 02:01:17 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:01:10 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | -0.101 |  |
| 2026-06-14 02:01:00 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.016 |  |
| 2026-06-14 02:00:50 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-06-14 01:36:37 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-14 01:33:58 | Putupaula (Kalu Ganga) | 2.71 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 01:04:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.54 | 🟠 Minor Flood | -0.010 |  |
| 2026-06-13 18:01:49 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-14 02:06:21 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:01:19 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:01:43 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-14 01:02:37 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:04:30 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:03:03 | Hanwella (Kelani Ganga) | 3.86 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:02:30 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:03:24 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:01:17 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:13:30 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:05:50 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-06-14 01:33:58 | Putupaula (Kalu Ganga) | 2.71 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:01:27 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:05:05 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:03:55 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-06-14 02:00:50 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-06-14 02:01:00 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.016 |  |
| 2026-06-14 01:04:23 | Giriulla (Maha Oya) | 2.14 | 🟢 Normal | -0.020 |  |
| 2026-06-14 02:05:32 | Baddegama (Gin Ganga) | 3.09 | 🟢 Normal | -0.020 |  |
| 2026-06-14 02:03:39 | Dunamale (Aththanagalu Oya) | 3.23 | 🟢 Normal | -0.020 |  |
| 2026-06-13 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.021 |  |
| 2026-06-14 02:02:13 | Ellagawa (Kalu Ganga) | 8.58 | 🟢 Normal | -0.021 |  |
| 2026-06-14 02:04:35 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.029 |  |
| 2026-06-14 02:06:17 | Badalgama (Maha Oya) | 3.28 | 🟢 Normal | -0.030 |  |
| 2026-06-14 02:01:25 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.030 |  |
| 2026-06-14 01:05:58 | Panadugama (Nilwala Ganga) | 4.18 | 🟢 Normal | -0.030 |  |
| 2026-06-14 01:03:27 | Holombuwa (Kelani Ganga) | 1.23 | 🟢 Normal | -0.032 |  |
| 2026-06-14 02:06:09 | Glencourse (Kelani Ganga) | 11.65 | 🟢 Normal | -0.033 |  |
| 2026-06-14 00:03:04 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.036 |  |
| 2026-06-14 02:04:19 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | -0.040 |  |
| 2026-06-13 18:05:47 | Galgamuwa (Mee Oya) | 1.44 | 🟢 Normal | -0.040 |  |
| 2026-06-14 02:01:18 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.042 |  |
| 2026-06-14 02:03:22 | Magura (Kalu Ganga) | 3.68 | 🟢 Normal | -0.053 |  |
| 2026-06-14 02:01:44 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.072 |  |
| 2026-06-14 01:05:23 | Rathnapura (Kalu Ganga) | 4.42 | 🟢 Normal | -0.090 |  |
| 2026-06-14 02:01:10 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | -0.101 |  |
| 2026-06-14 02:04:03 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -126.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)