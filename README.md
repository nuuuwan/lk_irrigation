# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--11_23:12:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **176,866 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 23:12:20 | Ellagawa (Kalu Ganga) | 6.65 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-06-11 23:11:35 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-11 23:11:02 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 23:10:17 | Thawalama (Gin Ganga) | 2.96 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-06-11 23:08:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.26 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-06-11 23:08:28 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-11 23:08:19 | Rathnapura (Kalu Ganga) | 5.59 | 🟡 Alert | 0.139 | 🔺 Rising |
| 2026-06-11 23:06:50 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-06-11 23:06:41 | Magura (Kalu Ganga) | 3.27 | 🟢 Normal | 0.285 | 🔺 Rising |
| 2026-06-11 23:05:44 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.063 |  |
| 2026-06-11 23:05:44 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-11 23:05:38 | Moraketiya (Walawe Ganga) | 1.24 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-11 23:05:32 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 23:05:30 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-06-11 23:05:03 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-06-11 23:04:33 | Moragaswewa (Deduru Oya) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-06-11 23:04:31 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-11 23:04:10 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-11 23:03:22 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-11 23:03:21 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-11 23:03:12 | Glencourse (Kelani Ganga) | 11.81 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-06-11 23:03:04 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-11 23:02:59 | Peradeniya (Mahaweli Ganga) | 2.23 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-11 23:02:43 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-11 23:02:33 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-11 23:02:29 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | 0.000 |  |
| 2026-06-11 23:02:19 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-11 23:02:17 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-11 23:02:13 | Deraniyagala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.169 |  |
| 2026-06-11 23:02:10 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-11 23:01:39 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 23:01:23 | Nawalapitiya (Mahaweli Ganga) | 2.11 | 🟢 Normal | -0.039 |  |
| 2026-06-11 23:01:01 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-11 23:00:46 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-11 22:37:19 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.063 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 23:08:19 | Rathnapura (Kalu Ganga) | 5.59 | 🟡 Alert | 0.139 | 🔺 Rising |
| 2026-06-11 23:06:41 | Magura (Kalu Ganga) | 3.27 | 🟢 Normal | 0.285 | 🔺 Rising |
| 2026-06-11 23:08:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.26 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-06-11 23:10:17 | Thawalama (Gin Ganga) | 2.96 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-06-11 23:03:12 | Glencourse (Kelani Ganga) | 11.81 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-06-11 23:12:20 | Ellagawa (Kalu Ganga) | 6.65 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-06-11 23:04:10 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-11 23:02:17 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-11 23:02:43 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-11 23:06:50 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-06-11 23:03:04 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-11 23:02:59 | Peradeniya (Mahaweli Ganga) | 2.23 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-11 22:08:37 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-06-11 23:11:35 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-11 23:03:22 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-11 23:08:28 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-11 23:05:44 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-11 23:04:31 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-11 23:05:32 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 23:05:38 | Moraketiya (Walawe Ganga) | 1.24 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-11 23:05:03 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-06-11 23:02:19 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-11 23:01:01 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-11 23:01:39 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 23:00:46 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-11 18:11:49 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-11 23:02:29 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | 0.000 |  |
| 2026-06-11 23:03:21 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-11 23:02:10 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-11 23:02:33 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-11 18:01:15 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-11 23:11:02 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 22:02:07 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-11 23:04:33 | Moragaswewa (Deduru Oya) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-06-11 23:05:30 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-06-11 18:00:24 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.021 |  |
| 2026-06-11 23:01:23 | Nawalapitiya (Mahaweli Ganga) | 2.11 | 🟢 Normal | -0.039 |  |
| 2026-06-11 23:05:44 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.063 |  |
| 2026-06-11 23:02:13 | Deraniyagala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.169 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)