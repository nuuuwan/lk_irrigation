# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--10_23:30:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **175,964 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-10 23:30:24 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:30:03 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:21:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.51 | 🟢 Normal | -0.008 |  |
| 2026-06-10 23:14:23 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | -0.018 |  |
| 2026-06-10 23:13:34 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:09:39 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:08:06 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:07:46 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:07:23 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:06:25 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:06:18 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-06-10 23:06:16 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:06:16 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-06-10 23:06:00 | Magura (Kalu Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:05:18 | Peradeniya (Mahaweli Ganga) | 2.19 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-06-10 23:05:16 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.049 |  |
| 2026-06-10 23:04:44 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:04:36 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:04:32 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.010 |  |
| 2026-06-10 23:04:11 | Hanwella (Kelani Ganga) | 2.48 | 🟢 Normal | -0.020 |  |
| 2026-06-10 23:03:58 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:03:31 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-10 23:03:19 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:03:09 | Glencourse (Kelani Ganga) | 10.56 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:02:41 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:02:14 | Rathnapura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-10 23:02:10 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:01:59 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:01:54 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:01:50 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-06-10 23:01:35 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | -0.060 |  |
| 2026-06-10 23:01:28 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 23:00:44 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:00:41 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:00:16 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-10 23:05:18 | Peradeniya (Mahaweli Ganga) | 2.19 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-06-10 23:02:14 | Rathnapura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-10 23:03:31 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-10 23:01:28 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 23:07:46 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:00:44 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:02:41 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-10 22:02:05 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:03:58 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:01:59 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:04:36 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:00:16 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-10 18:03:48 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:06:00 | Magura (Kalu Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:30:03 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:03:19 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:07:23 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:08:06 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:03:09 | Glencourse (Kelani Ganga) | 10.56 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:01:54 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:00:41 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:13:34 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:06:25 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:30:24 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:02:10 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-10 18:23:24 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:04:44 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:09:39 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:06:16 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:21:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.51 | 🟢 Normal | -0.008 |  |
| 2026-06-10 23:06:18 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-06-10 23:06:16 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-06-10 23:04:32 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.010 |  |
| 2026-06-10 23:14:23 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | -0.018 |  |
| 2026-06-10 23:04:11 | Hanwella (Kelani Ganga) | 2.48 | 🟢 Normal | -0.020 |  |
| 2026-06-10 18:01:23 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.020 |  |
| 2026-06-10 23:01:50 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-06-10 23:05:16 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.049 |  |
| 2026-06-10 23:01:35 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)