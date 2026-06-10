# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--10_21:18:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **175,891 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-10 21:18:54 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:14:37 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:12:40 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 21:11:49 | Glencourse (Kelani Ganga) | 10.56 | 🟢 Normal | -0.009 |  |
| 2026-06-10 21:10:44 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | -0.020 |  |
| 2026-06-10 21:10:43 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-10 21:10:06 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:09:27 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:08:28 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-10 21:07:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.54 | 🟢 Normal | -0.010 |  |
| 2026-06-10 21:07:07 | Baddegama (Gin Ganga) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-06-10 21:07:05 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:07:00 | Peradeniya (Mahaweli Ganga) | 1.94 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-06-10 21:07:00 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.101 |  |
| 2026-06-10 21:06:51 | Magura (Kalu Ganga) | 2.01 | 🟢 Normal | -36.000 |  |
| 2026-06-10 21:06:50 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | -36.000 |  |
| 2026-06-10 21:06:11 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-06-10 21:05:26 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:04:07 | Hanwella (Kelani Ganga) | 2.52 | 🟢 Normal | -0.020 |  |
| 2026-06-10 21:03:46 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-10 21:03:38 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:03:13 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-10 21:03:00 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:02:56 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | -0.010 |  |
| 2026-06-10 21:02:49 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-06-10 21:02:38 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:02:37 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:02:15 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:02:13 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | -0.049 |  |
| 2026-06-10 21:02:04 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:01:57 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-10 21:01:38 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:01:36 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:01:24 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 21:00:44 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:00:39 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-10 21:07:00 | Peradeniya (Mahaweli Ganga) | 1.94 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-06-10 21:10:43 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-10 21:01:57 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-10 21:03:46 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-10 21:03:13 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-10 20:02:44 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 21:01:24 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 21:12:40 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 21:08:28 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-10 21:00:39 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:00:44 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:03:38 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:03:00 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:18:54 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:01:36 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-10 18:03:48 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:02:15 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:09:27 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:14:37 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:02:38 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:01:38 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:02:37 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-10 18:23:24 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:02:04 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:05:26 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:07:05 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-10 21:11:49 | Glencourse (Kelani Ganga) | 10.56 | 🟢 Normal | -0.009 |  |
| 2026-06-10 21:07:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.54 | 🟢 Normal | -0.010 |  |
| 2026-06-10 21:06:11 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-06-10 21:02:56 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | -0.010 |  |
| 2026-06-10 21:02:49 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-06-10 21:10:44 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | -0.020 |  |
| 2026-06-10 21:04:07 | Hanwella (Kelani Ganga) | 2.52 | 🟢 Normal | -0.020 |  |
| 2026-06-10 21:07:07 | Baddegama (Gin Ganga) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-06-10 18:01:23 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.020 |  |
| 2026-06-10 21:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.021 |  |
| 2026-06-10 21:02:13 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | -0.049 |  |
| 2026-06-10 21:07:00 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.101 |  |
| 2026-06-10 21:06:51 | Magura (Kalu Ganga) | 2.01 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)