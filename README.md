# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--06_01:33:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **198,398 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-06 01:33:51 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.021 |  |
| 2026-07-06 01:18:14 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:17:40 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:17:14 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:16:17 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:13:58 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-07-06 01:13:10 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:08:39 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:07:52 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:07:41 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.667 |  |
| 2026-07-06 01:07:22 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:06:58 | Hanwella (Kelani Ganga) | 2.01 | 🟢 Normal | -0.048 |  |
| 2026-07-06 01:06:47 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.667 |  |
| 2026-07-06 01:06:06 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-06 01:05:26 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.203 |  |
| 2026-07-06 01:05:13 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 01:05:12 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-07-06 01:05:01 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:04:09 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-07-06 01:03:27 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:03:06 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.020 |  |
| 2026-07-06 01:02:54 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:02:49 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-07-06 01:02:34 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:02:06 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-07-06 01:01:58 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:01:24 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | -0.020 |  |
| 2026-07-06 01:01:14 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:01:00 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-06 01:04:09 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-07-06 00:16:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-07-06 01:06:06 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-06 01:13:58 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-07-06 01:05:13 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 00:00:14 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-06 00:01:38 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:01:00 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:17:14 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:16:17 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:05:41 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:18:14 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:03:27 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-06 00:06:00 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:02:54 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:07:22 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:17:40 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:02:34 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:01:14 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:08:39 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-05 23:01:42 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:05:01 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:03:25 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:07:52 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:01:58 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:13:10 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:05:12 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-07-06 00:03:36 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-07-05 18:00:08 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-07-06 00:01:59 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-07-05 23:07:35 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-07-06 01:02:49 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-07-06 01:03:06 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.020 |  |
| 2026-07-06 01:02:06 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-07-06 01:01:24 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | -0.020 |  |
| 2026-07-06 01:33:51 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.021 |  |
| 2026-07-06 01:06:58 | Hanwella (Kelani Ganga) | 2.01 | 🟢 Normal | -0.048 |  |
| 2026-07-06 01:05:26 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.203 |  |
| 2026-07-06 01:07:41 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.667 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)