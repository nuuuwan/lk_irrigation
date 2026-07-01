# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--01_22:12:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **194,714 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 22:12:25 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:11:11 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:10:50 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:07:56 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:07:31 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-07-01 22:07:30 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.049 |  |
| 2026-07-01 22:07:25 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:07:14 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.029 |  |
| 2026-07-01 22:06:58 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-07-01 22:06:03 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:05:56 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-07-01 22:05:47 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | -0.052 |  |
| 2026-07-01 22:05:26 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:05:26 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-07-01 22:04:59 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.186 |  |
| 2026-07-01 22:04:53 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:04:52 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-07-01 22:04:30 | Hanwella (Kelani Ganga) | 1.74 | 🟢 Normal | -0.020 |  |
| 2026-07-01 22:04:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | -0.019 |  |
| 2026-07-01 22:04:02 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:04:01 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:03:47 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:03:43 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:03:41 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 22:03:08 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-07-01 22:02:54 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:02:52 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:02:42 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-01 22:02:36 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:02:23 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.012 |  |
| 2026-07-01 22:02:03 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:01:46 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:01:37 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:01:37 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | -0.062 |  |
| 2026-07-01 22:01:19 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:00:12 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-01 21:36:28 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.045 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 22:04:52 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-07-01 22:03:08 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-07-01 22:02:42 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-01 22:03:41 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 18:02:29 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:02:54 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:01:19 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:06:03 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:02:52 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:01:37 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:04:53 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:02:03 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:06:53 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:12:25 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:01:46 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:11:11 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:03:47 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:10:50 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:00:12 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:03:43 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:07:25 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:02:36 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:02:02 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:07:56 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:04:01 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:04:02 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:07:31 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-07-01 22:06:58 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-07-01 22:05:26 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-07-01 22:05:56 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-07-01 22:02:23 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.012 |  |
| 2026-07-01 22:04:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | -0.019 |  |
| 2026-07-01 22:04:30 | Hanwella (Kelani Ganga) | 1.74 | 🟢 Normal | -0.020 |  |
| 2026-07-01 22:07:14 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.029 |  |
| 2026-07-01 22:07:30 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.049 |  |
| 2026-07-01 21:01:39 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.051 |  |
| 2026-07-01 22:05:47 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | -0.052 |  |
| 2026-07-01 22:01:37 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | -0.062 |  |
| 2026-07-01 22:04:59 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.186 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)