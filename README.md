# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--20_05:33:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **184,200 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 05:33:25 | Panadugama (Nilwala Ganga) | 5.32 | 🟡 Alert | 1.987 | 🔺 Rising |
| 2026-06-20 05:25:03 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.129 |  |
| 2026-06-20 05:11:40 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.009 |  |
| 2026-06-20 05:09:39 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.009 |  |
| 2026-06-20 05:08:27 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:08:00 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.014 |  |
| 2026-06-20 05:07:59 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:07:39 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:07:34 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.011 |  |
| 2026-06-20 05:07:18 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:07:01 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-06-20 05:06:58 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:05:59 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:05:22 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.023 |  |
| 2026-06-20 05:05:18 | Glencourse (Kelani Ganga) | 10.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:04:36 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:04:35 | Glencourse (Kelani Ganga) | 10.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:04:06 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:03:23 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-06-20 05:02:40 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:02:36 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.005 |  |
| 2026-06-20 05:02:24 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | -0.030 |  |
| 2026-06-20 05:02:12 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:02:06 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:01:51 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.015 |  |
| 2026-06-20 05:01:51 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:01:28 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:01:28 | Ellagawa (Kalu Ganga) | 5.59 | 🟢 Normal | -0.020 |  |
| 2026-06-20 05:01:21 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-20 05:01:13 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.161 |  |
| 2026-06-20 05:01:13 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:01:10 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:00:54 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:00:42 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:00:27 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:44:45 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 05:33:25 | Panadugama (Nilwala Ganga) | 5.32 | 🟡 Alert | 1.987 | 🔺 Rising |
| 2026-06-20 05:03:23 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-06-20 05:01:21 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-20 05:07:39 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:00:15 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:00:42 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:00:54 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:00:27 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:01:51 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:02:40 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:04:06 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:02:46 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:04:36 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:07:18 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:08:27 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:01:13 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:05:18 | Glencourse (Kelani Ganga) | 10.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:01:10 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:02:12 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:05:59 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:07:59 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:01:28 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:02:43 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:02:06 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:02:36 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.005 |  |
| 2026-06-20 05:11:40 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.009 |  |
| 2026-06-20 05:09:39 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.009 |  |
| 2026-06-20 05:07:01 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-06-19 18:02:43 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-06-20 05:07:34 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.011 |  |
| 2026-06-20 05:08:00 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.014 |  |
| 2026-06-20 05:01:51 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.015 |  |
| 2026-06-20 05:01:28 | Ellagawa (Kalu Ganga) | 5.59 | 🟢 Normal | -0.020 |  |
| 2026-06-20 05:05:22 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.023 |  |
| 2026-06-20 04:04:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.79 | 🟢 Normal | -0.028 |  |
| 2026-06-20 05:02:24 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | -0.030 |  |
| 2026-06-20 04:02:45 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.030 |  |
| 2026-06-20 05:25:03 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.129 |  |
| 2026-06-20 05:01:13 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.161 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)