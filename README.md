# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--22_00:13:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **185,816 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 00:13:50 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:13:10 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:12:29 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:07:16 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:07:13 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.005 |  |
| 2026-06-22 00:06:21 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:05:47 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-22 00:05:40 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-06-22 00:05:36 | Hanwella (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:05:18 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:05:12 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:04:59 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:04:56 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.036 |  |
| 2026-06-22 00:04:54 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.029 |  |
| 2026-06-22 00:04:17 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:04:03 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-22 00:03:44 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-06-22 00:03:26 | Glencourse (Kelani Ganga) | 10.14 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-06-22 00:02:59 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:02:50 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-06-22 00:02:47 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-22 00:02:33 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:02:15 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 00:01:47 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:01:39 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:01:38 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:01:36 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:01:20 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:01:00 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:00:39 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:30:19 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 00:05:40 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-06-22 00:03:44 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-06-22 00:03:26 | Glencourse (Kelani Ganga) | 10.14 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-06-22 00:02:50 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-06-21 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-22 00:05:47 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-22 00:04:03 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-22 00:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-22 00:02:15 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 00:13:50 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:01:38 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:01:39 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:06:21 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:02:26 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:04:17 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:01:20 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:07:51 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:13:10 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:02:47 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:05:36 | Hanwella (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:05:12 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:12:29 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:01:00 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:00:39 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:04:59 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:02:59 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:07:16 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:02:33 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:01:15 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:01:47 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-22 00:07:13 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.005 |  |
| 2026-06-21 21:01:51 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-21 18:01:51 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-06-21 23:04:40 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.021 |  |
| 2026-06-22 00:04:54 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.029 |  |
| 2026-06-22 00:04:56 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.036 |  |
| 2026-06-21 23:07:57 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.040 |  |
| 2026-06-21 23:14:17 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)