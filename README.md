# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--08_08:06:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **200,452 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-08 08:06:23 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-07-08 08:06:12 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.029 |  |
| 2026-07-08 08:05:46 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.011 |  |
| 2026-07-08 08:05:34 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:05:34 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:05:11 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:04:58 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:04:50 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-08 08:04:26 | Hanwella (Kelani Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-07-08 08:04:06 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.021 |  |
| 2026-07-08 08:03:52 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-08 08:03:36 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:03:29 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.068 |  |
| 2026-07-08 08:03:28 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-07-08 08:03:23 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:03:23 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:02:54 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:02:37 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:02:37 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.05 | 🟢 Normal | -0.110 |  |
| 2026-07-08 08:02:26 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:02:23 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:02:13 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | -0.010 |  |
| 2026-07-08 08:02:10 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:01:49 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-08 08:01:43 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:01:17 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.357 |  |
| 2026-07-08 08:01:08 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:00:48 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:00:46 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:00:31 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:00:17 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:47:08 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:41:43 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-08 08:04:50 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-08 08:01:49 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-08 08:03:52 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-08 08:01:08 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:00:17 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:05:34 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:02:37 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:02:23 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:01:43 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:05:34 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:10:00 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:02:54 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:03:23 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:03:36 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:41:43 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:02:26 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:00:48 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:03:23 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:05:11 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:02:37 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:04:58 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:02:10 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:03:14 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:00:46 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:00:31 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-08 07:03:38 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-08 08:04:26 | Hanwella (Kelani Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-07-08 08:02:13 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | -0.010 |  |
| 2026-07-08 08:03:28 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-07-08 08:06:23 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-07-08 08:05:46 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.011 |  |
| 2026-07-08 08:04:06 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.021 |  |
| 2026-07-08 08:06:12 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.029 |  |
| 2026-07-08 07:03:59 | Glencourse (Kelani Ganga) | 9.58 | 🟢 Normal | -0.040 |  |
| 2026-07-08 08:03:29 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.068 |  |
| 2026-07-08 08:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.05 | 🟢 Normal | -0.110 |  |
| 2026-07-08 07:10:28 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.214 |  |
| 2026-07-08 08:01:17 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.357 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)