# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--06_23:17:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **199,228 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-06 23:17:30 | Ellagawa (Kalu Ganga) | 0.00 | 🟢 Normal | -3.903 |  |
| 2026-07-06 23:10:47 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:10:37 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-06 23:10:05 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-07-06 23:09:26 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:08:07 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-06 23:07:34 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:07:22 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 23:05:16 | Badalgama (Maha Oya) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-07-06 23:05:12 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:04:23 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.092 |  |
| 2026-07-06 23:04:21 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:04:16 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:03:43 | Peradeniya (Mahaweli Ganga) | 2.61 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-07-06 23:03:18 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:03:00 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | -0.040 |  |
| 2026-07-06 23:02:54 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.140 |  |
| 2026-07-06 23:02:43 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:02:39 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 23:02:17 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:02:16 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:02:02 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:01:40 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:01:21 | Dunamale (Aththanagalu Oya) | 1.27 | 🟢 Normal | -0.022 |  |
| 2026-07-06 23:00:55 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:00:53 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-07-06 23:00:44 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:00:15 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:00:09 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-06 23:03:43 | Peradeniya (Mahaweli Ganga) | 2.61 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-07-06 23:08:07 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-06 23:10:37 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-06 22:02:33 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-06 22:06:00 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 23:02:39 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 23:07:22 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 23:00:55 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:04:16 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:00:44 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-06 22:01:36 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:00:09 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:02:16 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:02:17 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:04:21 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:07:34 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:03:18 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:00:15 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:02:43 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-06 22:03:15 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:10:47 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-06 18:00:56 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:05:12 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:09:26 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:01:40 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:02:02 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-06 23:10:05 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-07-06 22:13:34 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-07-06 18:02:06 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-07-06 18:06:11 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-07-06 23:00:53 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-07-06 23:05:16 | Badalgama (Maha Oya) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-07-06 23:01:21 | Dunamale (Aththanagalu Oya) | 1.27 | 🟢 Normal | -0.022 |  |
| 2026-07-06 20:07:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.024 |  |
| 2026-07-06 23:03:00 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | -0.040 |  |
| 2026-07-06 22:14:59 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.040 |  |
| 2026-07-06 23:04:23 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.092 |  |
| 2026-07-06 23:02:54 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.140 |  |
| 2026-07-06 23:17:30 | Ellagawa (Kalu Ganga) | 0.00 | 🟢 Normal | -3.903 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)