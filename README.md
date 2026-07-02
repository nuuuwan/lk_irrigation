# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--03_03:23:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **195,775 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-03 03:23:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | 612.000 | 🔺 Rising |
| 2026-07-03 03:23:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | 612.000 | 🔺 Rising |
| 2026-07-03 03:22:52 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.894 |  |
| 2026-07-03 03:17:10 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-03 03:15:08 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:14:49 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.894 |  |
| 2026-07-03 03:09:04 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:08:39 | Glencourse (Kelani Ganga) | 9.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 03:08:17 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -18.000 |  |
| 2026-07-03 03:08:15 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | -18.000 |  |
| 2026-07-03 03:08:07 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:07:42 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:06:53 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.163 |  |
| 2026-07-03 03:06:45 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-03 03:06:37 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:06:07 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-07-03 03:06:01 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-07-03 03:05:26 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:05:23 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | -18.000 |  |
| 2026-07-03 03:04:31 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:04:03 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 03:03:59 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.052 |  |
| 2026-07-03 03:03:56 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:03:31 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:03:22 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-03 03:03:09 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:02:48 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:02:42 | Rathnapura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-07-03 03:02:25 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:02:15 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:01:53 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:01:53 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 03:01:04 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:01:00 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 03:00:59 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:00:50 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.008 |  |
| 2026-07-03 03:00:30 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-03 03:23:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | 612.000 | 🔺 Rising |
| 2026-07-03 03:06:01 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-07-03 01:23:15 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-07-03 03:03:22 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-03 03:17:10 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-03 03:06:45 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-03 03:01:53 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 03:08:39 | Glencourse (Kelani Ganga) | 9.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 03:01:00 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 03:04:03 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 02:45:04 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-07-02 18:00:16 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:01:04 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:00:59 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:01:53 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:03:09 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:02:48 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:01:58 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:15:08 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:02:15 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:08:07 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:03:56 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:02:25 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:03:31 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:09:04 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:05:26 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:07:42 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:51:10 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-03 02:45:18 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:04:31 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:06:37 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-03 03:00:50 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.008 |  |
| 2026-07-03 03:02:42 | Rathnapura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-07-03 03:06:07 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-07-03 03:03:59 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.052 |  |
| 2026-07-03 03:06:53 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.163 |  |
| 2026-07-03 03:22:52 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.894 |  |
| 2026-07-03 03:08:17 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)