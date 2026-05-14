# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_10:03:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **151,468 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 10:03:31 | Putupaula (Kalu Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-05-14 10:03:18 | Hanwella (Kelani Ganga) | 2.29 | 🟢 Normal | -0.061 |  |
| 2026-05-14 10:02:59 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-14 10:02:37 | Manampitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-14 10:02:35 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-14 10:02:28 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.073 |  |
| 2026-05-14 10:02:27 | Baddegama (Gin Ganga) | 3.25 | 🟢 Normal | -0.021 |  |
| 2026-05-14 10:02:22 | Thanthirimale (Malwathu Oya) | 3.28 | 🟢 Normal | 0.000 |  |
| 2026-05-14 10:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.37 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-14 10:02:21 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.060 |  |
| 2026-05-14 10:02:00 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.120 |  |
| 2026-05-14 10:01:54 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-14 10:01:18 | Ellagawa (Kalu Ganga) | 8.26 | 🟢 Normal | -0.011 |  |
| 2026-05-14 10:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-05-14 10:01:15 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-05-14 10:01:10 | Dunamale (Aththanagalu Oya) | 2.98 | 🟢 Normal | -0.061 |  |
| 2026-05-14 10:01:05 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.010 |  |
| 2026-05-14 10:00:54 | Moraketiya (Walawe Ganga) | 1.43 | 🟢 Normal | -0.180 |  |
| 2026-05-14 10:00:52 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-14 10:00:36 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-05-14 09:15:42 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.082 |  |
| 2026-05-14 09:11:29 | Magura (Kalu Ganga) | 4.26 | 🟡 Alert | -0.019 |  |
| 2026-05-14 09:11:25 | Galgamuwa (Mee Oya) | 2.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 10:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.37 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-14 09:11:29 | Magura (Kalu Ganga) | 4.26 | 🟡 Alert | -0.019 |  |
| 2026-05-14 09:06:13 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-05-14 10:00:52 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-14 09:06:00 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-14 10:01:54 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-14 09:05:23 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-14 09:11:25 | Galgamuwa (Mee Oya) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-05-14 09:03:31 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-14 10:02:59 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-14 10:02:35 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-14 09:03:11 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-14 09:02:23 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-14 10:03:31 | Putupaula (Kalu Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-05-14 10:02:22 | Thanthirimale (Malwathu Oya) | 3.28 | 🟢 Normal | 0.000 |  |
| 2026-05-14 09:00:08 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-14 09:02:04 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-05-14 10:02:37 | Manampitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-14 10:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-05-14 10:01:15 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-05-14 10:01:05 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.010 |  |
| 2026-05-14 09:03:44 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-05-14 10:01:18 | Ellagawa (Kalu Ganga) | 8.26 | 🟢 Normal | -0.011 |  |
| 2026-05-14 09:07:22 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.011 |  |
| 2026-05-14 10:00:36 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-05-14 10:02:27 | Baddegama (Gin Ganga) | 3.25 | 🟢 Normal | -0.021 |  |
| 2026-05-14 09:01:34 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.023 |  |
| 2026-05-14 09:02:59 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | -0.041 |  |
| 2026-05-14 09:03:28 | Moragaswewa (Deduru Oya) | 1.52 | 🟢 Normal | -0.043 |  |
| 2026-05-14 09:01:41 | Glencourse (Kelani Ganga) | 10.19 | 🟢 Normal | -0.054 |  |
| 2026-05-14 10:02:21 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.060 |  |
| 2026-05-14 10:01:10 | Dunamale (Aththanagalu Oya) | 2.98 | 🟢 Normal | -0.061 |  |
| 2026-05-14 10:03:18 | Hanwella (Kelani Ganga) | 2.29 | 🟢 Normal | -0.061 |  |
| 2026-05-14 09:06:16 | Panadugama (Nilwala Ganga) | 4.23 | 🟢 Normal | -0.068 |  |
| 2026-05-14 10:02:28 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.073 |  |
| 2026-05-14 09:03:42 | Rathnapura (Kalu Ganga) | 4.28 | 🟢 Normal | -0.080 |  |
| 2026-05-14 09:15:42 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.082 |  |
| 2026-05-14 10:02:00 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.120 |  |
| 2026-05-14 10:00:54 | Moraketiya (Walawe Ganga) | 1.43 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)