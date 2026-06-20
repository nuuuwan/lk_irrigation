# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--20_20:13:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **184,776 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 20:13:33 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-06-20 20:11:56 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.009 |  |
| 2026-06-20 20:11:54 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.026 |  |
| 2026-06-20 20:10:27 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.022 |  |
| 2026-06-20 20:10:04 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-06-20 20:09:57 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-20 20:08:58 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-20 20:08:24 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-20 20:07:44 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.123 |  |
| 2026-06-20 20:07:30 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-06-20 20:06:46 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.022 |  |
| 2026-06-20 20:05:52 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.018 |  |
| 2026-06-20 20:05:49 | Glencourse (Kelani Ganga) | 9.71 | 🟢 Normal | -0.041 |  |
| 2026-06-20 20:05:05 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 20:04:36 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | -0.048 |  |
| 2026-06-20 20:04:27 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-06-20 20:04:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.98 | 🟢 Normal | -0.010 |  |
| 2026-06-20 20:04:15 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-06-20 20:03:57 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.088 |  |
| 2026-06-20 20:03:28 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.109 |  |
| 2026-06-20 20:03:26 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-20 20:03:19 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-20 20:02:58 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-06-20 20:02:32 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.022 |  |
| 2026-06-20 20:02:27 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 20:02:22 | Dunamale (Aththanagalu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-06-20 20:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-06-20 20:02:01 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-20 20:01:54 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-20 20:01:31 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 20:01:20 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-20 20:01:17 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 20:01:17 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | -0.020 |  |
| 2026-06-20 20:01:13 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 20:04:15 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-06-20 20:03:19 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-20 20:08:24 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-20 18:12:10 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-20 20:02:01 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-20 20:01:54 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-20 20:01:17 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 20:03:26 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-20 20:01:31 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 20:07:30 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-06-20 20:05:05 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 20:01:20 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-20 20:01:06 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 20:02:22 | Dunamale (Aththanagalu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-06-20 20:09:57 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-20 20:08:58 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-20 20:01:13 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 20:02:27 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 20:11:56 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.009 |  |
| 2026-06-20 20:10:04 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-06-20 20:13:33 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-06-20 20:00:16 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-06-20 18:02:49 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-06-20 20:02:58 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-06-20 20:04:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.98 | 🟢 Normal | -0.010 |  |
| 2026-06-20 18:00:20 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.011 |  |
| 2026-06-20 20:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-06-20 20:04:27 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-06-20 20:05:52 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.018 |  |
| 2026-06-20 20:01:17 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | -0.020 |  |
| 2026-06-20 20:02:32 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.022 |  |
| 2026-06-20 20:06:46 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.022 |  |
| 2026-06-20 20:10:27 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.022 |  |
| 2026-06-20 20:11:54 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.026 |  |
| 2026-06-20 20:05:49 | Glencourse (Kelani Ganga) | 9.71 | 🟢 Normal | -0.041 |  |
| 2026-06-20 20:04:36 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | -0.048 |  |
| 2026-06-20 20:03:57 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.088 |  |
| 2026-06-20 20:03:28 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.109 |  |
| 2026-06-20 20:07:44 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)