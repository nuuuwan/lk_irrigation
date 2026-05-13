# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_00:32:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **151,118 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 00:32:33 | Dunamale (Aththanagalu Oya) | 3.48 | 🟡 Alert | 0.000 |  |
| 2026-05-14 00:23:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.90 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-05-14 00:23:22 | Urawa (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.024 |  |
| 2026-05-14 00:12:12 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | -5.723 |  |
| 2026-05-14 00:11:32 | Giriulla (Maha Oya) | 2.16 | 🟢 Normal | -0.078 |  |
| 2026-05-14 00:09:54 | Thanamalwila (Kirindi Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-14 00:09:30 | Ellagawa (Kalu Ganga) | 8.22 | 🟢 Normal | 0.000 |  |
| 2026-05-14 00:08:01 | Kuda Oya (Kirindi Oya) | 1.73 | 🟢 Normal | -0.009 |  |
| 2026-05-14 00:07:54 | Putupaula (Kalu Ganga) | 2.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-14 00:06:14 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-05-14 00:05:59 | Rathnapura (Kalu Ganga) | 5.49 | 🟡 Alert | -0.129 |  |
| 2026-05-14 00:05:54 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-14 00:05:45 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.050 |  |
| 2026-05-14 00:05:43 | Panadugama (Nilwala Ganga) | 4.92 | 🟢 Normal | -0.195 |  |
| 2026-05-14 00:05:43 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-05-14 00:05:41 | Baddegama (Gin Ganga) | 3.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-14 00:05:28 | Hanwella (Kelani Ganga) | 2.87 | 🟢 Normal | -0.030 |  |
| 2026-05-14 00:04:29 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-05-14 00:04:07 | Thawalama (Gin Ganga) | 2.74 | 🟢 Normal | -0.060 |  |
| 2026-05-14 00:03:55 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -1.064 |  |
| 2026-05-14 00:03:37 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-14 00:03:36 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-14 00:03:36 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-05-14 00:03:35 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | -0.152 |  |
| 2026-05-14 00:03:12 | Ellagawa (Kalu Ganga) | 8.22 | 🟢 Normal | 0.000 |  |
| 2026-05-14 00:02:54 | Manampitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.048 |  |
| 2026-05-14 00:02:38 | Magura (Kalu Ganga) | 5.07 | 🟡 Alert | -0.040 |  |
| 2026-05-14 00:02:22 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-05-14 00:01:43 | Badalgama (Maha Oya) | 3.29 | 🟢 Normal | -5.723 |  |
| 2026-05-14 00:01:39 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.095 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 00:23:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.90 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-05-14 00:32:33 | Dunamale (Aththanagalu Oya) | 3.48 | 🟡 Alert | 0.000 |  |
| 2026-05-14 00:02:38 | Magura (Kalu Ganga) | 5.07 | 🟡 Alert | -0.040 |  |
| 2026-05-14 00:05:59 | Rathnapura (Kalu Ganga) | 5.49 | 🟡 Alert | -0.129 |  |
| 2026-05-14 00:01:39 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-05-13 18:02:23 | Galgamuwa (Mee Oya) | 2.97 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-14 00:05:41 | Baddegama (Gin Ganga) | 3.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-14 00:07:54 | Putupaula (Kalu Ganga) | 2.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-13 18:02:22 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 00:05:54 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-14 00:00:46 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-14 00:00:42 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-14 00:09:30 | Ellagawa (Kalu Ganga) | 8.22 | 🟢 Normal | 0.000 |  |
| 2026-05-14 00:00:15 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-14 00:03:37 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-13 23:06:39 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-14 00:01:03 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-14 00:09:54 | Thanamalwila (Kirindi Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-14 00:08:01 | Kuda Oya (Kirindi Oya) | 1.73 | 🟢 Normal | -0.009 |  |
| 2026-05-14 00:02:22 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-05-14 00:06:14 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-05-14 00:03:36 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-05-14 00:04:29 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-05-14 00:05:43 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-05-14 00:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-05-14 00:01:27 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | -0.022 |  |
| 2026-05-14 00:23:22 | Urawa (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.024 |  |
| 2026-05-14 00:05:28 | Hanwella (Kelani Ganga) | 2.87 | 🟢 Normal | -0.030 |  |
| 2026-05-14 00:02:54 | Manampitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.048 |  |
| 2026-05-14 00:05:45 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.050 |  |
| 2026-05-13 18:02:14 | Thanthirimale (Malwathu Oya) | 3.35 | 🟢 Normal | -0.051 |  |
| 2026-05-14 00:01:21 | Pitabeddara (Nilwala Ganga) | 1.49 | 🟢 Normal | -0.052 |  |
| 2026-05-14 00:04:07 | Thawalama (Gin Ganga) | 2.74 | 🟢 Normal | -0.060 |  |
| 2026-05-13 23:04:55 | Moragaswewa (Deduru Oya) | 2.70 | 🟢 Normal | -0.076 |  |
| 2026-05-14 00:11:32 | Giriulla (Maha Oya) | 2.16 | 🟢 Normal | -0.078 |  |
| 2026-05-14 00:03:35 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | -0.152 |  |
| 2026-05-14 00:05:43 | Panadugama (Nilwala Ganga) | 4.92 | 🟢 Normal | -0.195 |  |
| 2026-05-14 00:03:55 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -1.064 |  |
| 2026-05-14 00:12:12 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | -5.723 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)