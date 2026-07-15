# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--15_22:10:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **207,256 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-15 22:10:49 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:09:20 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:08:29 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:07:54 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:07:43 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-07-15 22:05:35 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-15 22:05:26 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:05:14 | Putupaula (Kalu Ganga) | 0.10 | 🟢 Normal | -0.060 |  |
| 2026-07-15 22:04:35 | Nagalagam Street (Kelani Ganga) | 0.03 | 🟢 Normal | -0.032 |  |
| 2026-07-15 22:04:28 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:04:18 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:04:04 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:03:35 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:03:25 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:03:09 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.011 |  |
| 2026-07-15 22:03:09 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:03:06 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:03:06 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:03:01 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:02:59 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | -0.039 |  |
| 2026-07-15 22:02:54 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.034 |  |
| 2026-07-15 22:02:46 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-07-15 22:02:31 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:02:27 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-07-15 22:01:47 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:01:37 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:00:54 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:00:52 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.020 |  |
| 2026-07-15 22:00:50 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:00:39 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:00:33 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:00:28 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-15 21:02:39 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | 0.421 | 🔺 Rising |
| 2026-07-15 22:05:35 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-15 21:08:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-15 22:02:31 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:00:28 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:00:54 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:00:33 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:01:37 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:08:29 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:00:39 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-15 18:02:45 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:07:54 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:05:26 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:03:06 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:10:49 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:00:50 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:03:35 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:03:01 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:03:25 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:03:09 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:03:06 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:04:04 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:04:18 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-15 21:10:06 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:04:28 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:09:20 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-15 22:01:47 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-15 18:14:35 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | -0.008 |  |
| 2026-07-15 22:07:43 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-07-15 22:02:27 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-07-15 22:02:46 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-07-15 22:03:09 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.011 |  |
| 2026-07-15 21:12:45 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.018 |  |
| 2026-07-15 22:00:52 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.020 |  |
| 2026-07-15 22:04:35 | Nagalagam Street (Kelani Ganga) | 0.03 | 🟢 Normal | -0.032 |  |
| 2026-07-15 22:02:54 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.034 |  |
| 2026-07-15 22:02:59 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | -0.039 |  |
| 2026-07-15 22:05:14 | Putupaula (Kalu Ganga) | 0.10 | 🟢 Normal | -0.060 |  |
| 2026-07-15 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)