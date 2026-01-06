# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--06_08:27:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **38,015 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 08:27:22 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.016 |  |
| 2026-01-06 08:18:16 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-06 08:17:26 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-01-06 08:14:03 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.033 |  |
| 2026-01-06 08:11:09 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-06 08:10:58 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-06 08:09:02 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.350 | 🔺 Rising |
| 2026-01-06 08:08:44 | Panadugama (Nilwala Ganga) | 2.97 | 🟢 Normal | -0.016 |  |
| 2026-01-06 08:08:37 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-06 08:08:21 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 08:08:04 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.021 |  |
| 2026-01-06 08:07:35 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-01-06 08:07:20 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.009 |  |
| 2026-01-06 08:06:38 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.116 |  |
| 2026-01-06 08:06:23 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-01-06 08:05:06 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-06 08:04:18 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-06 08:04:13 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-06 08:04:11 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-06 08:03:56 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.030 |  |
| 2026-01-06 08:03:41 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.015 |  |
| 2026-01-06 08:03:30 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-06 08:03:13 | Nakkala (Kumbukkan Oya) | 1.54 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-01-06 08:03:06 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 08:02:59 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-06 08:02:58 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-06 08:02:56 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-01-06 08:02:46 | Padiyathalawa (Maduru Oya) | 2.50 | 🟢 Normal | 0.302 | 🔺 Rising |
| 2026-01-06 08:02:39 | Thaldena (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-01-06 08:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-01-06 08:02:15 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 08:02:09 | Manampitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-01-06 08:02:03 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 08:01:49 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.132 |  |
| 2026-01-06 08:01:33 | Siyambalanduwa (Heda Oya) | 4.20 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-06 08:01:18 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-01-06 08:01:10 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-01-06 08:01:00 | Weraganthota (Mahaweli Ganga) | -0.47 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-06 08:00:10 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 08:09:02 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.350 | 🔺 Rising |
| 2026-01-06 08:02:46 | Padiyathalawa (Maduru Oya) | 2.50 | 🟢 Normal | 0.302 | 🔺 Rising |
| 2026-01-06 08:02:09 | Manampitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-01-06 08:03:13 | Nakkala (Kumbukkan Oya) | 1.54 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-01-06 08:07:35 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-01-06 08:02:39 | Thaldena (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-01-06 08:01:00 | Weraganthota (Mahaweli Ganga) | -0.47 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-06 08:04:13 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-06 08:05:06 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-06 08:01:33 | Siyambalanduwa (Heda Oya) | 4.20 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-06 08:02:59 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-06 08:01:18 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-01-06 08:18:16 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-06 08:04:18 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-06 08:04:11 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-06 08:17:26 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-01-06 08:08:37 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-06 08:02:03 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 08:02:15 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 08:03:06 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 08:10:58 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-06 08:11:09 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-06 08:08:21 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 08:00:10 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-06 08:01:10 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-01-06 08:06:23 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-01-06 08:03:30 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-06 08:07:20 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.009 |  |
| 2026-01-06 08:02:56 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-01-06 08:02:58 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-06 08:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-01-06 08:03:41 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.015 |  |
| 2026-01-06 08:27:22 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.016 |  |
| 2026-01-06 08:08:44 | Panadugama (Nilwala Ganga) | 2.97 | 🟢 Normal | -0.016 |  |
| 2026-01-06 08:08:04 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.021 |  |
| 2026-01-06 08:03:56 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.030 |  |
| 2026-01-06 08:14:03 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.033 |  |
| 2026-01-06 08:06:38 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.116 |  |
| 2026-01-06 08:01:49 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.132 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)