# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--07_05:09:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **66,234 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 05:09:12 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.010 |  |
| 2026-02-07 05:07:45 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -9.000 |  |
| 2026-02-07 05:07:17 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -9.000 |  |
| 2026-02-07 05:07:01 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.048 |  |
| 2026-02-07 05:06:55 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-07 05:06:53 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:06:40 | Horowpothana (Yan Oya) | 2.80 | 🟢 Normal | -0.047 |  |
| 2026-02-07 05:06:35 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.037 |  |
| 2026-02-07 05:06:06 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-07 05:05:59 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-02-07 05:05:33 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:05:03 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-07 05:04:47 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.41 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-02-07 05:03:58 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -18.000 |  |
| 2026-02-07 05:03:56 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -18.000 |  |
| 2026-02-07 05:03:44 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:03:35 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:03:24 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:03:11 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:03:00 | Padiyathalawa (Maduru Oya) | 1.04 | 🟢 Normal | -0.039 |  |
| 2026-02-07 05:02:52 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:02:22 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:02:16 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:01:59 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:01:57 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-07 05:01:43 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-02-07 05:01:25 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:01:15 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | -0.630 |  |
| 2026-02-07 05:00:48 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.461 |  |
| 2026-02-07 04:41:16 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.461 |  |
| 2026-02-07 04:28:46 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-02-07 04:28:38 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:27:10 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:26:02 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.630 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 05:05:59 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-02-07 05:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.41 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-07 05:01:57 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-07 05:06:55 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-07 04:09:19 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-07 05:05:33 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:02:52 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:28:38 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:03:35 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:04:57 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:18:04 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:03:11 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:27:10 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:01:59 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:03:44 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:01:25 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:04:47 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:03:24 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:03:13 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:05:33 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:02:16 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-07 05:06:53 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:04:23 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.003 |  |
| 2026-02-07 04:11:03 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | -0.005 |  |
| 2026-02-07 05:09:12 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.010 |  |
| 2026-02-07 05:05:03 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-07 05:01:43 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-02-07 05:06:06 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-07 05:06:35 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.037 |  |
| 2026-02-07 05:03:00 | Padiyathalawa (Maduru Oya) | 1.04 | 🟢 Normal | -0.039 |  |
| 2026-02-06 18:01:44 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | -0.039 |  |
| 2026-02-07 05:06:40 | Horowpothana (Yan Oya) | 2.80 | 🟢 Normal | -0.047 |  |
| 2026-02-07 05:07:01 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.048 |  |
| 2026-02-07 05:00:48 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.461 |  |
| 2026-02-07 05:01:15 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | -0.630 |  |
| 2026-02-07 05:07:45 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -9.000 |  |
| 2026-02-07 05:03:58 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)