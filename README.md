# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_18:25:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **158,968 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 18:25:06 | Baddegama (Gin Ganga) | 2.43 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-05-22 18:12:33 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:11:25 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:10:09 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:07:58 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-05-22 18:07:37 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-22 18:06:25 | Rathnapura (Kalu Ganga) | 7.50 | 🟠 Minor Flood | -0.083 |  |
| 2026-05-22 18:05:32 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-05-22 18:05:29 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:05:26 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.075 |  |
| 2026-05-22 18:05:19 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:04:51 | Ellagawa (Kalu Ganga) | 9.37 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-22 18:04:23 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | -0.042 |  |
| 2026-05-22 18:04:17 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-05-22 18:04:17 | Glencourse (Kelani Ganga) | 15.10 | 🟡 Alert | -0.151 |  |
| 2026-05-22 18:04:08 | Magura (Kalu Ganga) | 4.38 | 🟡 Alert | -0.043 |  |
| 2026-05-22 18:03:54 | Nagalagam Street (Kelani Ganga) | 1.46 | 🟡 Alert | 0.000 |  |
| 2026-05-22 18:03:21 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:03:13 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:03:11 | Deraniyagala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.061 |  |
| 2026-05-22 18:03:00 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:02:58 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:02:54 | Giriulla (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:02:39 | Badalgama (Maha Oya) | 3.85 | 🟢 Normal | -0.021 |  |
| 2026-05-22 18:02:32 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-22 18:02:32 | Hanwella (Kelani Ganga) | 8.12 | 🟠 Minor Flood | -0.020 |  |
| 2026-05-22 18:02:32 | Dunamale (Aththanagalu Oya) | 5.12 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2026-05-22 18:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.87 | 🟡 Alert | 0.080 | 🔺 Rising |
| 2026-05-22 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.030 |  |
| 2026-05-22 18:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-05-22 18:01:59 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:01:41 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.034 |  |
| 2026-05-22 18:01:36 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-22 18:01:33 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-22 18:01:21 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:00:49 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-05-22 18:00:38 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-22 18:00:34 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:00:16 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:00:07 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-05-22 17:58:32 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 18:02:32 | Dunamale (Aththanagalu Oya) | 5.12 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2026-05-22 18:02:32 | Hanwella (Kelani Ganga) | 8.12 | 🟠 Minor Flood | -0.020 |  |
| 2026-05-22 18:06:25 | Rathnapura (Kalu Ganga) | 7.50 | 🟠 Minor Flood | -0.083 |  |
| 2026-05-22 18:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.87 | 🟡 Alert | 0.080 | 🔺 Rising |
| 2026-05-22 18:03:54 | Nagalagam Street (Kelani Ganga) | 1.46 | 🟡 Alert | 0.000 |  |
| 2026-05-22 18:04:08 | Magura (Kalu Ganga) | 4.38 | 🟡 Alert | -0.043 |  |
| 2026-05-22 18:04:17 | Glencourse (Kelani Ganga) | 15.10 | 🟡 Alert | -0.151 |  |
| 2026-05-22 18:04:17 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-05-22 18:07:58 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-05-22 18:25:06 | Baddegama (Gin Ganga) | 2.43 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-05-22 18:00:38 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-22 18:01:33 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-22 18:04:51 | Ellagawa (Kalu Ganga) | 9.37 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-22 18:01:36 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-22 18:07:37 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-22 18:00:34 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:02:58 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:05:19 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:02:54 | Giriulla (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:01:21 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:03:13 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:10:09 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:00:16 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:03:21 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:12:33 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:11:25 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:03:00 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:01:59 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:05:32 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-05-22 18:02:32 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-22 18:00:49 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-05-22 18:00:07 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-05-22 18:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-05-22 18:02:39 | Badalgama (Maha Oya) | 3.85 | 🟢 Normal | -0.021 |  |
| 2026-05-22 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.030 |  |
| 2026-05-22 18:01:41 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.034 |  |
| 2026-05-22 18:04:23 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | -0.042 |  |
| 2026-05-22 18:03:11 | Deraniyagala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.061 |  |
| 2026-05-22 18:05:26 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.075 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)