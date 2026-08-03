# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_09:21:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **223,653 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 09:21:20 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-08-03 09:13:04 | Glencourse (Kelani Ganga) | 14.35 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:12:47 | Glencourse (Kelani Ganga) | 14.35 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:12:09 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:11:23 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.062 |  |
| 2026-08-03 09:10:22 | Kithulgala (Kelani Ganga) | 2.71 | 🟢 Normal | -0.057 |  |
| 2026-08-03 09:10:02 | Pitabeddara (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.232 |  |
| 2026-08-03 09:09:32 | Norwood (Kelani Ganga) | 2.18 | 🟡 Alert | 0.150 | 🔺 Rising |
| 2026-08-03 09:09:13 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:08:20 | Rathnapura (Kalu Ganga) | 6.55 | 🟡 Alert | -0.048 |  |
| 2026-08-03 09:08:03 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:08:01 | Panadugama (Nilwala Ganga) | 3.89 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:07:41 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.088 |  |
| 2026-08-03 09:07:38 | Ellagawa (Kalu Ganga) | 7.18 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-08-03 09:07:00 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 09:06:13 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.021 |  |
| 2026-08-03 09:05:39 | Baddegama (Gin Ganga) | 2.26 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-03 09:05:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.00 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-08-03 09:04:49 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:04:36 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:04:36 | Hanwella (Kelani Ganga) | 4.77 | 🟢 Normal | 0.324 | 🔺 Rising |
| 2026-08-03 09:04:10 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:04:09 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-03 09:03:42 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:03:20 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:02:55 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:02:53 | Deraniyagala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.201 |  |
| 2026-08-03 09:02:39 | Thanamalwila (Kirindi Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:02:35 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-03 09:02:34 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 09:02:33 | Peradeniya (Mahaweli Ganga) | 7.15 | 🟠 Minor Flood | -0.152 |  |
| 2026-08-03 09:02:30 | Thawalama (Gin Ganga) | 2.37 | 🟢 Normal | -0.085 |  |
| 2026-08-03 09:02:21 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:02:19 | Nawalapitiya (Mahaweli Ganga) | 4.08 | 🟡 Alert | -0.216 |  |
| 2026-08-03 09:02:11 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:02:06 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:01:48 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.020 |  |
| 2026-08-03 09:01:31 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:01:29 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 09:00:42 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-03 09:00:11 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 09:02:33 | Peradeniya (Mahaweli Ganga) | 7.15 | 🟠 Minor Flood | -0.152 |  |
| 2026-08-03 09:09:32 | Norwood (Kelani Ganga) | 2.18 | 🟡 Alert | 0.150 | 🔺 Rising |
| 2026-08-03 09:08:20 | Rathnapura (Kalu Ganga) | 6.55 | 🟡 Alert | -0.048 |  |
| 2026-08-03 09:02:19 | Nawalapitiya (Mahaweli Ganga) | 4.08 | 🟡 Alert | -0.216 |  |
| 2026-08-03 09:04:36 | Hanwella (Kelani Ganga) | 4.77 | 🟢 Normal | 0.324 | 🔺 Rising |
| 2026-08-03 09:07:38 | Ellagawa (Kalu Ganga) | 7.18 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-08-03 09:05:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.00 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-08-03 09:04:09 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-03 09:05:39 | Baddegama (Gin Ganga) | 2.26 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-03 09:00:42 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-03 09:02:35 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-03 09:01:29 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 09:07:00 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 09:02:34 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 09:02:21 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:04:49 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:02:11 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:02:55 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:01:31 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:04:36 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:08:01 | Panadugama (Nilwala Ganga) | 3.89 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:09:13 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:13:04 | Glencourse (Kelani Ganga) | 14.35 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:03:20 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:03:42 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:04:10 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:12:09 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:08:03 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:00:11 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:02:39 | Thanamalwila (Kirindi Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-03 09:21:20 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-08-03 09:01:48 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.020 |  |
| 2026-08-03 09:06:13 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.021 |  |
| 2026-08-03 09:10:22 | Kithulgala (Kelani Ganga) | 2.71 | 🟢 Normal | -0.057 |  |
| 2026-08-03 09:11:23 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.062 |  |
| 2026-08-03 09:02:30 | Thawalama (Gin Ganga) | 2.37 | 🟢 Normal | -0.085 |  |
| 2026-08-03 09:07:41 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.088 |  |
| 2026-08-03 09:02:53 | Deraniyagala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.201 |  |
| 2026-08-03 09:10:02 | Pitabeddara (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.232 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)