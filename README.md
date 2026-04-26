# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--27_05:14:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **136,139 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 05:14:25 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-27 05:12:23 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-27 05:12:06 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.009 |  |
| 2026-04-27 05:11:57 | Rathnapura (Kalu Ganga) | 1.77 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-04-27 05:10:09 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-27 05:08:54 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 252.000 | 🔺 Rising |
| 2026-04-27 05:08:53 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 252.000 | 🔺 Rising |
| 2026-04-27 05:07:14 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-04-27 05:05:32 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-27 05:05:09 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-27 05:04:58 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.019 |  |
| 2026-04-27 05:04:49 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-27 05:04:44 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-27 05:04:31 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-27 05:04:28 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-27 05:04:11 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.029 |  |
| 2026-04-27 05:03:34 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | -0.108 |  |
| 2026-04-27 05:03:28 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-27 05:03:11 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-27 05:03:10 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-27 05:02:59 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-27 05:02:50 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-27 05:02:45 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-27 05:02:28 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-27 05:02:21 | Glencourse (Kelani Ganga) | 9.02 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-04-27 05:01:44 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-27 05:01:38 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 05:01:30 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-27 05:01:19 | Peradeniya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.070 |  |
| 2026-04-27 05:01:17 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-27 05:01:12 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 05:00:40 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.021 |  |
| 2026-04-27 05:00:38 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-27 04:37:38 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 05:08:54 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 252.000 | 🔺 Rising |
| 2026-04-27 05:11:57 | Rathnapura (Kalu Ganga) | 1.77 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-04-27 05:07:14 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-04-27 05:02:21 | Glencourse (Kelani Ganga) | 9.02 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-04-27 05:02:59 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-27 04:08:49 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-27 05:10:09 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-27 05:00:38 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-27 05:02:45 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-27 05:04:44 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-27 05:01:30 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-27 05:04:31 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-27 05:03:28 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-27 05:04:49 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-26 18:00:28 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-27 05:01:12 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 05:14:25 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-27 05:01:38 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 05:02:50 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-27 05:12:23 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-27 05:03:10 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-27 05:02:28 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-27 05:04:28 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-27 05:01:44 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-27 05:05:32 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-27 05:01:17 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-26 18:06:09 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.009 |  |
| 2026-04-27 05:12:06 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.009 |  |
| 2026-04-27 04:08:07 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-04-27 03:00:14 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-04-27 05:04:58 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.019 |  |
| 2026-04-27 05:00:40 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.021 |  |
| 2026-04-27 05:04:11 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.029 |  |
| 2026-04-26 18:03:51 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-04-27 04:03:18 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.061 |  |
| 2026-04-27 05:01:19 | Peradeniya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.070 |  |
| 2026-04-27 05:03:34 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | -0.108 |  |
| 2026-04-26 20:08:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.123 |  |
| 2026-04-27 04:06:46 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)