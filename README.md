# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--20_19:22:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **184,740 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 19:22:43 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:15:36 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.025 |  |
| 2026-06-20 19:11:43 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:11:02 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:10:34 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.009 |  |
| 2026-06-20 19:09:41 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-20 19:07:51 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | -0.046 |  |
| 2026-06-20 19:07:38 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-06-20 19:06:51 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:06:44 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:06:29 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.011 |  |
| 2026-06-20 19:06:21 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:05:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.99 | 🟢 Normal | -0.028 |  |
| 2026-06-20 19:05:42 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:05:32 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:05:30 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:04:14 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.019 |  |
| 2026-06-20 19:04:12 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:04:12 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-20 19:03:49 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:03:27 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:02:44 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | -0.123 |  |
| 2026-06-20 19:02:37 | Hanwella (Kelani Ganga) | 1.91 | 🟢 Normal | -0.050 |  |
| 2026-06-20 19:02:37 | Dunamale (Aththanagalu Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-06-20 19:02:34 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:02:27 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:02:15 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:01:54 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:01:44 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.027 |  |
| 2026-06-20 19:01:43 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | -0.030 |  |
| 2026-06-20 19:01:36 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:01:31 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:01:28 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.060 |  |
| 2026-06-20 19:01:18 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:00:52 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:00:25 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-06-20 19:00:13 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 19:04:12 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-20 19:07:38 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-06-20 19:09:41 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-20 18:12:10 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-20 19:00:13 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:01:54 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:22:43 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:06:51 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:01:31 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:03:49 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:00:52 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:11:43 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:11:02 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:02:27 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:01:18 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:01:36 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:02:15 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:03:27 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:04:12 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:05:30 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:06:44 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:05:42 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:06:21 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:05:32 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 19:10:34 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.009 |  |
| 2026-06-20 19:02:37 | Dunamale (Aththanagalu Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-06-20 18:02:49 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-06-20 19:00:25 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-06-20 18:00:20 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.011 |  |
| 2026-06-20 19:06:29 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.011 |  |
| 2026-06-20 19:04:14 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.019 |  |
| 2026-06-20 19:15:36 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.025 |  |
| 2026-06-20 19:01:44 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.027 |  |
| 2026-06-20 19:05:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.99 | 🟢 Normal | -0.028 |  |
| 2026-06-20 19:01:43 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | -0.030 |  |
| 2026-06-20 19:07:51 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | -0.046 |  |
| 2026-06-20 19:02:37 | Hanwella (Kelani Ganga) | 1.91 | 🟢 Normal | -0.050 |  |
| 2026-06-20 19:01:28 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.060 |  |
| 2026-06-20 19:02:44 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)