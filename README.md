# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--09_08:07:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **201,346 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-09 08:07:22 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | -0.009 |  |
| 2026-07-09 08:06:45 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-07-09 08:06:36 | Peradeniya (Mahaweli Ganga) | 1.88 | 🟢 Normal | 0.287 | 🔺 Rising |
| 2026-07-09 08:05:43 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:05:25 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:05:05 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.047 |  |
| 2026-07-09 08:04:45 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:04:35 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-07-09 08:04:29 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:04:20 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:04:09 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:04:02 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:03:39 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:03:33 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.031 |  |
| 2026-07-09 08:03:31 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:02:59 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:02:50 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:02:43 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.79 | 🟢 Normal | -0.080 |  |
| 2026-07-09 08:02:35 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.020 |  |
| 2026-07-09 08:02:33 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-07-09 08:02:26 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:02:19 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-09 08:02:13 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-09 08:01:51 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:01:47 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:01:38 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:01:31 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:01:28 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:01:27 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:01:23 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-09 08:01:23 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:01:03 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:00:48 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:00:18 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:23:56 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:17:52 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-09 08:06:36 | Peradeniya (Mahaweli Ganga) | 1.88 | 🟢 Normal | 0.287 | 🔺 Rising |
| 2026-07-09 08:02:13 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-09 08:01:23 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-09 08:02:19 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-09 08:02:26 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:01:38 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:01:51 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:04:02 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:03:21 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:02:43 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:00:48 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:03:31 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:02:50 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:03:39 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:01:23 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:04:20 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:01:28 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:04:09 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:04:04 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:01:03 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:05:25 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:04:29 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:02:59 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:01:27 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:05:43 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:14:06 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:00:18 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:01:31 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-09 08:01:47 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-09 07:09:28 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.009 |  |
| 2026-07-09 08:07:22 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | -0.009 |  |
| 2026-07-09 07:05:05 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.009 |  |
| 2026-07-09 08:06:45 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-07-09 08:02:33 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-07-09 08:02:35 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.020 |  |
| 2026-07-09 08:04:35 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-07-09 08:03:33 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.031 |  |
| 2026-07-09 08:05:05 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.047 |  |
| 2026-07-09 08:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.79 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)