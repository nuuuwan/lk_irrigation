# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_17:13:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **172,189 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 17:13:46 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-06-06 17:13:19 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-06 17:09:48 | Rathnapura (Kalu Ganga) | 3.11 | 🟢 Normal | -0.050 |  |
| 2026-06-06 17:09:33 | Putupaula (Kalu Ganga) | 1.59 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-06 17:09:00 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-06-06 17:08:36 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-06-06 17:07:03 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-06 17:05:13 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | -0.029 |  |
| 2026-06-06 17:04:38 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-06-06 17:04:14 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-06 17:04:07 | Baddegama (Gin Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-06-06 17:03:48 | Nawalapitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.020 |  |
| 2026-06-06 17:03:38 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-06 17:03:34 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-06 17:03:29 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | -0.013 |  |
| 2026-06-06 17:03:28 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-06-06 17:03:18 | Hanwella (Kelani Ganga) | 3.34 | 🟢 Normal | -0.030 |  |
| 2026-06-06 17:03:15 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-06-06 17:03:08 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-06 17:03:08 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 17:03:07 | Deraniyagala (Kelani Ganga) | 1.37 | 🟢 Normal | -0.108 |  |
| 2026-06-06 17:03:04 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-06 17:03:01 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.275 | 🔺 Rising |
| 2026-06-06 17:03:01 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-06-06 17:02:49 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-06-06 17:02:33 | Glencourse (Kelani Ganga) | 11.17 | 🟢 Normal | -0.041 |  |
| 2026-06-06 17:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.19 | 🟢 Normal | -0.020 |  |
| 2026-06-06 17:02:25 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-06-06 17:02:14 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.030 |  |
| 2026-06-06 17:02:07 | Dunamale (Aththanagalu Oya) | 3.02 | 🟢 Normal | -0.070 |  |
| 2026-06-06 17:01:55 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-06 17:01:36 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-06 17:01:25 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-06 17:01:17 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-06 17:01:08 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-06 17:01:07 | Ellagawa (Kalu Ganga) | 7.28 | 🟢 Normal | -0.010 |  |
| 2026-06-06 17:01:01 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-06-06 17:00:44 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-06 17:00:39 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 17:03:01 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.275 | 🔺 Rising |
| 2026-06-06 17:08:36 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-06-06 17:13:46 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-06-06 17:04:38 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-06-06 17:07:03 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-06 17:09:33 | Putupaula (Kalu Ganga) | 1.59 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-06 17:01:17 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-06 17:13:19 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-06 17:01:36 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-06 17:01:55 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-06 17:00:39 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 17:03:04 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-06 17:04:14 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-06 17:03:38 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-06 17:04:07 | Baddegama (Gin Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-06-06 17:09:00 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-06-06 17:03:08 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 17:01:25 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-06 17:00:44 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-06 17:03:08 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-06 17:01:08 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-06 17:03:34 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-06 17:03:15 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-06-06 17:02:25 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-06-06 17:01:07 | Ellagawa (Kalu Ganga) | 7.28 | 🟢 Normal | -0.010 |  |
| 2026-06-06 17:02:49 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-06-06 17:01:01 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-06-06 17:03:01 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-06-06 17:03:28 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-06-06 17:03:29 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | -0.013 |  |
| 2026-06-06 17:03:48 | Nawalapitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.020 |  |
| 2026-06-06 17:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.19 | 🟢 Normal | -0.020 |  |
| 2026-06-06 17:05:13 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | -0.029 |  |
| 2026-06-06 17:03:18 | Hanwella (Kelani Ganga) | 3.34 | 🟢 Normal | -0.030 |  |
| 2026-06-06 17:02:14 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.030 |  |
| 2026-06-06 17:02:33 | Glencourse (Kelani Ganga) | 11.17 | 🟢 Normal | -0.041 |  |
| 2026-06-06 17:09:48 | Rathnapura (Kalu Ganga) | 3.11 | 🟢 Normal | -0.050 |  |
| 2026-06-06 17:02:07 | Dunamale (Aththanagalu Oya) | 3.02 | 🟢 Normal | -0.070 |  |
| 2026-06-06 17:03:07 | Deraniyagala (Kelani Ganga) | 1.37 | 🟢 Normal | -0.108 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)