# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--23_12:03:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **187,147 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 12:03:10 | Panadugama (Nilwala Ganga) | 3.95 | 🟢 Normal | -0.033 |  |
| 2026-06-23 12:03:03 | Giriulla (Maha Oya) | 2.48 | 🟢 Normal | -0.050 |  |
| 2026-06-23 12:02:54 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-23 12:02:52 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-06-23 12:02:48 | Badalgama (Maha Oya) | 3.64 | 🟢 Normal | -0.031 |  |
| 2026-06-23 12:02:19 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.022 |  |
| 2026-06-23 12:02:18 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-23 12:02:12 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-23 12:02:09 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 12:02:08 | Dunamale (Aththanagalu Oya) | 4.08 | 🟡 Alert | 0.000 |  |
| 2026-06-23 12:01:59 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.046 |  |
| 2026-06-23 12:01:45 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-06-23 12:01:44 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-23 12:01:39 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.206 |  |
| 2026-06-23 12:01:39 | Ellagawa (Kalu Ganga) | 8.12 | 🟢 Normal | 0.000 |  |
| 2026-06-23 12:01:38 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 12:01:36 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 12:01:27 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.010 |  |
| 2026-06-23 12:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-06-23 12:01:21 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 12:01:09 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-23 12:01:02 | Pitabeddara (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.069 |  |
| 2026-06-23 12:00:51 | Magura (Kalu Ganga) | 3.38 | 🟢 Normal | -0.103 |  |
| 2026-06-23 12:00:27 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-23 11:26:09 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.023 |  |
| 2026-06-23 11:23:38 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-06-23 11:21:05 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 11:03:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.95 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-06-23 12:02:08 | Dunamale (Aththanagalu Oya) | 4.08 | 🟡 Alert | 0.000 |  |
| 2026-06-23 11:02:05 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-23 11:11:23 | Putupaula (Kalu Ganga) | 2.33 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-23 11:23:38 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-06-23 12:01:21 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 12:01:38 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 12:00:27 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-23 12:02:54 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-23 12:01:36 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 11:05:09 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-23 12:01:39 | Ellagawa (Kalu Ganga) | 8.12 | 🟢 Normal | 0.000 |  |
| 2026-06-23 11:11:42 | Baddegama (Gin Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-06-23 12:02:09 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 11:05:36 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-23 12:02:12 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-23 12:01:45 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-06-23 12:01:44 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-23 11:21:05 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-23 12:01:09 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-23 12:02:18 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-23 12:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-06-23 12:01:27 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.010 |  |
| 2026-06-23 12:02:52 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-06-23 12:02:19 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.022 |  |
| 2026-06-23 11:26:09 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.023 |  |
| 2026-06-23 12:02:48 | Badalgama (Maha Oya) | 3.64 | 🟢 Normal | -0.031 |  |
| 2026-06-23 12:03:10 | Panadugama (Nilwala Ganga) | 3.95 | 🟢 Normal | -0.033 |  |
| 2026-06-23 12:01:59 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.046 |  |
| 2026-06-23 11:04:42 | Holombuwa (Kelani Ganga) | 1.12 | 🟢 Normal | -0.050 |  |
| 2026-06-23 12:03:03 | Giriulla (Maha Oya) | 2.48 | 🟢 Normal | -0.050 |  |
| 2026-06-23 12:01:02 | Pitabeddara (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.069 |  |
| 2026-06-23 11:04:54 | Hanwella (Kelani Ganga) | 4.87 | 🟢 Normal | -0.079 |  |
| 2026-06-23 11:05:19 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.095 |  |
| 2026-06-23 12:00:51 | Magura (Kalu Ganga) | 3.38 | 🟢 Normal | -0.103 |  |
| 2026-06-23 11:01:45 | Peradeniya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.116 |  |
| 2026-06-23 11:07:38 | Rathnapura (Kalu Ganga) | 3.34 | 🟢 Normal | -0.153 |  |
| 2026-06-23 11:06:47 | Glencourse (Kelani Ganga) | 12.31 | 🟢 Normal | -0.178 |  |
| 2026-06-23 12:01:39 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.206 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)