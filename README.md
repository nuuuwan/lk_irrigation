# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_14:14:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **150,745 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 14:14:51 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-13 14:09:38 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-13 14:08:38 | Magura (Kalu Ganga) | 5.03 | 🟡 Alert | 0.168 | 🔺 Rising |
| 2026-05-13 14:08:13 | Holombuwa (Kelani Ganga) | 1.12 | 🟢 Normal | -0.191 |  |
| 2026-05-13 14:08:11 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-05-13 14:08:02 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.046 |  |
| 2026-05-13 14:07:51 | Rathnapura (Kalu Ganga) | 6.28 | 🟡 Alert | 0.028 | 🔺 Rising |
| 2026-05-13 14:07:08 | Baddegama (Gin Ganga) | 2.84 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-05-13 14:06:39 | Katharagama (Menik Ganga) | 0.91 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-13 14:06:12 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-13 14:06:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.34 | 🟡 Alert | 0.131 | 🔺 Rising |
| 2026-05-13 14:05:51 | Panadugama (Nilwala Ganga) | 4.90 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-05-13 14:05:31 | Deraniyagala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.143 |  |
| 2026-05-13 14:05:12 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-05-13 14:04:24 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 14:04:18 | Dunamale (Aththanagalu Oya) | 3.22 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-05-13 14:04:12 | Putupaula (Kalu Ganga) | 2.07 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-13 14:04:07 | Galgamuwa (Mee Oya) | 2.80 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-05-13 14:03:54 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.061 |  |
| 2026-05-13 14:03:41 | Wellawaya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-05-13 14:03:39 | Kuda Oya (Kirindi Oya) | 1.81 | 🟢 Normal | -0.022 |  |
| 2026-05-13 14:03:31 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 14:03:29 | Hanwella (Kelani Ganga) | 2.25 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-13 14:03:09 | Urawa (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.021 |  |
| 2026-05-13 14:03:04 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-05-13 14:02:43 | Ellagawa (Kalu Ganga) | 7.62 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-05-13 14:02:42 | Moragaswewa (Deduru Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-05-13 14:02:39 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.089 |  |
| 2026-05-13 14:02:15 | Moraketiya (Walawe Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-05-13 14:02:05 | Thanamalwila (Kirindi Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-13 14:01:49 | Thanthirimale (Malwathu Oya) | 3.50 | 🟢 Normal | 0.000 |  |
| 2026-05-13 14:01:43 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-13 14:01:43 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 14:01:38 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-13 14:01:35 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-05-13 14:01:11 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.032 |  |
| 2026-05-13 14:00:13 | Pitabeddara (Nilwala Ganga) | 2.53 | 🟢 Normal | -0.022 |  |
| 2026-05-13 14:00:09 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 14:08:38 | Magura (Kalu Ganga) | 5.03 | 🟡 Alert | 0.168 | 🔺 Rising |
| 2026-05-13 14:06:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.34 | 🟡 Alert | 0.131 | 🔺 Rising |
| 2026-05-13 14:07:51 | Rathnapura (Kalu Ganga) | 6.28 | 🟡 Alert | 0.028 | 🔺 Rising |
| 2026-05-13 14:05:51 | Panadugama (Nilwala Ganga) | 4.90 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-05-13 14:08:11 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-05-13 14:04:18 | Dunamale (Aththanagalu Oya) | 3.22 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-05-13 14:05:12 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-05-13 14:01:43 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-13 14:02:43 | Ellagawa (Kalu Ganga) | 7.62 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-05-13 14:07:08 | Baddegama (Gin Ganga) | 2.84 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-05-13 14:03:29 | Hanwella (Kelani Ganga) | 2.25 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-13 14:04:07 | Galgamuwa (Mee Oya) | 2.80 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-05-13 14:04:12 | Putupaula (Kalu Ganga) | 2.07 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-13 14:06:39 | Katharagama (Menik Ganga) | 0.91 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-13 14:06:12 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-13 14:01:38 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-13 14:04:24 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 14:03:31 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 14:00:09 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | 0.000 |  |
| 2026-05-13 14:02:42 | Moragaswewa (Deduru Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-05-13 14:01:43 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 14:14:51 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-13 14:09:38 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-13 14:02:15 | Moraketiya (Walawe Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-05-13 14:01:49 | Thanthirimale (Malwathu Oya) | 3.50 | 🟢 Normal | 0.000 |  |
| 2026-05-13 14:02:05 | Thanamalwila (Kirindi Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-13 14:03:41 | Wellawaya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-05-13 14:03:04 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-05-13 14:01:35 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-05-13 14:03:09 | Urawa (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.021 |  |
| 2026-05-13 14:03:39 | Kuda Oya (Kirindi Oya) | 1.81 | 🟢 Normal | -0.022 |  |
| 2026-05-13 14:00:13 | Pitabeddara (Nilwala Ganga) | 2.53 | 🟢 Normal | -0.022 |  |
| 2026-05-13 13:05:45 | Thawalama (Gin Ganga) | 3.47 | 🟢 Normal | -0.028 |  |
| 2026-05-13 14:01:11 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.032 |  |
| 2026-05-13 14:08:02 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.046 |  |
| 2026-05-13 14:03:54 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.061 |  |
| 2026-05-13 14:02:39 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.089 |  |
| 2026-05-13 14:05:31 | Deraniyagala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.143 |  |
| 2026-05-13 14:08:13 | Holombuwa (Kelani Ganga) | 1.12 | 🟢 Normal | -0.191 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)