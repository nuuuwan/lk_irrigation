# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_17:15:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **198,110 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 17:15:24 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-07-05 17:14:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.01 | 🟢 Normal | -0.058 |  |
| 2026-07-05 17:13:46 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:11:23 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:09:54 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.037 |  |
| 2026-07-05 17:08:24 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | -0.048 |  |
| 2026-07-05 17:07:15 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.026 |  |
| 2026-07-05 17:06:58 | Dunamale (Aththanagalu Oya) | 1.41 | 🟢 Normal | -0.009 |  |
| 2026-07-05 17:06:44 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-05 17:06:22 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:05:29 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | -0.058 |  |
| 2026-07-05 17:04:14 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-07-05 17:04:11 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:04:07 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:04:00 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:03:56 | Hanwella (Kelani Ganga) | 2.51 | 🟢 Normal | -0.091 |  |
| 2026-07-05 17:03:40 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:03:20 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-07-05 17:03:05 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-07-05 17:02:42 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:02:38 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-05 17:02:14 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:02:01 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-07-05 17:01:55 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.020 |  |
| 2026-07-05 17:01:52 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-05 17:01:44 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:01:26 | Ellagawa (Kalu Ganga) | 5.36 | 🟢 Normal | -0.061 |  |
| 2026-07-05 17:01:23 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:01:16 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:01:04 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-07-05 17:00:57 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:00:57 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:00:42 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:00:19 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:00:15 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 17:02:38 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-05 17:01:52 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-05 17:06:44 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-05 16:05:33 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-05 17:01:23 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:00:57 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:00:15 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:03:40 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:06:45 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:00:57 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:00:42 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:09:15 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:00:19 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:13:46 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:02:42 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:01:16 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:04:07 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:02:14 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:04:00 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:04:11 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:06:22 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:11:23 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:01:44 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 17:15:24 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-07-05 17:06:58 | Dunamale (Aththanagalu Oya) | 1.41 | 🟢 Normal | -0.009 |  |
| 2026-07-05 17:03:05 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-07-05 17:01:04 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-07-05 17:02:01 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-07-05 16:02:37 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-07-05 17:04:14 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-07-05 17:01:55 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.020 |  |
| 2026-07-05 17:03:20 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-07-05 17:07:15 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.026 |  |
| 2026-07-05 17:09:54 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.037 |  |
| 2026-07-05 17:08:24 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | -0.048 |  |
| 2026-07-05 17:14:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.01 | 🟢 Normal | -0.058 |  |
| 2026-07-05 17:05:29 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | -0.058 |  |
| 2026-07-05 17:01:26 | Ellagawa (Kalu Ganga) | 5.36 | 🟢 Normal | -0.061 |  |
| 2026-07-05 17:03:56 | Hanwella (Kelani Ganga) | 2.51 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)