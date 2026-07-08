# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--09_02:08:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **201,120 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-09 02:08:22 | Glencourse (Kelani Ganga) | 9.57 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-07-09 02:08:19 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:07:27 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:07:08 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:07:05 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:07:01 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:06:59 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:06:57 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:06:54 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:06:48 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:06:41 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:06:20 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:05:52 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.039 |  |
| 2026-07-09 02:04:52 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:04:33 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:03:28 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:03:26 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-07-09 02:03:12 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-09 02:02:55 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:02:28 | Ellagawa (Kalu Ganga) | 4.49 | 🟢 Normal | -0.011 |  |
| 2026-07-09 02:02:15 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-09 02:02:06 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:01:55 | Hanwella (Kelani Ganga) | 1.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-09 02:01:35 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:01:32 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:01:20 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-07-09 02:01:19 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-09 01:59:17 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-09 01:42:28 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-07-09 01:36:25 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-09 01:32:54 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.023 |  |
| 2026-07-09 01:31:10 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-08 20:03:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | 2.448 | 🔺 Rising |
| 2026-07-09 01:05:49 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-07-09 02:08:22 | Glencourse (Kelani Ganga) | 9.57 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-07-09 02:03:12 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-09 02:01:55 | Hanwella (Kelani Ganga) | 1.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-09 02:02:15 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-09 02:02:06 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-09 01:03:02 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:01:35 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:03:28 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:01:19 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:06:59 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-08 17:08:44 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-09 01:06:18 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-08 22:05:09 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-09 01:03:05 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:06:48 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-07-09 01:31:10 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-07-09 00:03:17 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:02:55 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:04:52 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:06:57 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:04:33 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:07:08 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:06:54 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-07-08 18:01:29 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:01:32 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:07:01 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:08:19 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:07:05 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:07:27 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-09 02:03:26 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-07-09 02:01:20 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-07-09 02:02:28 | Ellagawa (Kalu Ganga) | 4.49 | 🟢 Normal | -0.011 |  |
| 2026-07-08 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.021 |  |
| 2026-07-09 01:32:54 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.023 |  |
| 2026-07-09 00:02:45 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.030 |  |
| 2026-07-09 02:05:52 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.039 |  |
| 2026-07-09 01:03:14 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)