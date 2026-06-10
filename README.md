# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--11_00:20:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **175,994 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 00:20:24 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:11:55 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:11:52 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:09:37 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:08:28 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:08:28 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.027 |  |
| 2026-06-11 00:08:20 | Rathnapura (Kalu Ganga) | 1.81 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-06-11 00:08:03 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-11 00:08:01 | Hanwella (Kelani Ganga) | 2.46 | 🟢 Normal | -0.019 |  |
| 2026-06-11 00:07:53 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:07:29 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:07:13 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:06:35 | Glencourse (Kelani Ganga) | 10.56 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:05:51 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:05:37 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-06-11 00:05:29 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-06-11 00:04:32 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-06-11 00:04:26 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | -0.029 |  |
| 2026-06-11 00:04:04 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-06-11 00:04:03 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 00:03:15 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-06-11 00:02:28 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:02:17 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:02:09 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:02:05 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:01:56 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:01:56 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-11 00:01:33 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | -0.011 |  |
| 2026-06-11 00:01:32 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:01:26 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 00:04:04 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-06-11 00:08:03 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-11 00:08:20 | Rathnapura (Kalu Ganga) | 1.81 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-06-11 00:01:56 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-11 00:04:03 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-10 23:03:31 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-11 00:02:28 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:01:32 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:20:24 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:11:52 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:00:16 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-10 18:03:48 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:06:00 | Magura (Kalu Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:08:28 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:05:51 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:11:55 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:07:23 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:01:56 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:06:35 | Glencourse (Kelani Ganga) | 10.56 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:07:13 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:02:17 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:02:05 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:09:37 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:30:24 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:02:09 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-10 18:23:24 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:09:39 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:07:53 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:21:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.51 | 🟢 Normal | -0.008 |  |
| 2026-06-10 23:06:18 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-06-11 00:05:37 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-06-11 00:03:15 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-06-11 00:01:33 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | -0.011 |  |
| 2026-06-11 00:08:01 | Hanwella (Kelani Ganga) | 2.46 | 🟢 Normal | -0.019 |  |
| 2026-06-11 00:05:29 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-06-11 00:04:32 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-06-10 18:01:23 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.020 |  |
| 2026-06-11 00:08:28 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.027 |  |
| 2026-06-11 00:04:26 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | -0.029 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)