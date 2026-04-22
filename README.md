# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_04:34:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **132,533 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 04:34:32 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-23 04:23:33 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.033 |  |
| 2026-04-23 04:22:36 | Rathnapura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.054 |  |
| 2026-04-23 04:21:37 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-23 04:17:50 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.041 |  |
| 2026-04-23 04:15:44 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -11.455 |  |
| 2026-04-23 04:15:22 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -11.455 |  |
| 2026-04-23 04:07:43 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-04-23 04:07:41 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-04-23 04:07:09 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-04-23 04:07:01 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-23 04:05:32 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 04:04:28 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.025 |  |
| 2026-04-23 04:03:48 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-23 04:03:48 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-04-23 04:03:38 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-23 04:03:35 | Glencourse (Kelani Ganga) | 9.56 | 🟢 Normal | 0.307 | 🔺 Rising |
| 2026-04-23 04:03:13 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | -0.041 |  |
| 2026-04-23 04:03:11 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-23 04:02:52 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.019 |  |
| 2026-04-23 04:02:43 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-04-23 04:02:23 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.019 |  |
| 2026-04-23 04:02:11 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-04-23 04:02:11 | Thanamalwila (Kirindi Oya) | 2.41 | 🟢 Normal | -0.168 |  |
| 2026-04-23 04:01:54 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-23 04:01:54 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-23 04:01:22 | Kuda Oya (Kirindi Oya) | 2.06 | 🟢 Normal | -0.040 |  |
| 2026-04-23 04:01:22 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-23 04:01:21 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.116 |  |
| 2026-04-23 04:01:21 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-04-23 04:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-04-23 04:01:01 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.030 |  |
| 2026-04-23 04:00:26 | Manampitiya (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 04:07:43 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-04-23 03:34:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | 0.673 | 🔺 Rising |
| 2026-04-23 04:03:35 | Glencourse (Kelani Ganga) | 9.56 | 🟢 Normal | 0.307 | 🔺 Rising |
| 2026-04-23 04:02:43 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-04-23 04:01:21 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-04-23 04:03:11 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-23 04:01:22 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-23 04:34:32 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-23 04:03:38 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-22 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-23 04:07:01 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-23 04:21:37 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-23 04:05:32 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 03:01:06 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-23 04:01:54 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-23 04:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-04-23 04:01:54 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-23 04:03:48 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-23 04:03:48 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-04-23 04:02:11 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-04-22 18:02:04 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-04-22 18:02:52 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-23 04:02:52 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.019 |  |
| 2026-04-23 04:02:23 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.019 |  |
| 2026-04-23 04:07:09 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-04-23 04:04:28 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.025 |  |
| 2026-04-23 04:01:01 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.030 |  |
| 2026-04-23 04:00:26 | Manampitiya (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.031 |  |
| 2026-04-23 04:23:33 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.033 |  |
| 2026-04-23 00:07:57 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.039 |  |
| 2026-04-23 04:01:22 | Kuda Oya (Kirindi Oya) | 2.06 | 🟢 Normal | -0.040 |  |
| 2026-04-23 04:17:50 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.041 |  |
| 2026-04-23 04:22:36 | Rathnapura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.054 |  |
| 2026-04-23 03:00:48 | Moraketiya (Walawe Ganga) | 1.57 | 🟢 Normal | -0.080 |  |
| 2026-04-23 03:10:46 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.098 |  |
| 2026-04-23 04:01:21 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.116 |  |
| 2026-04-23 04:02:11 | Thanamalwila (Kirindi Oya) | 2.41 | 🟢 Normal | -0.168 |  |
| 2026-04-23 04:15:44 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -11.455 |  |
| 2026-04-23 03:11:52 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)