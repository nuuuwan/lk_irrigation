# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--18_16:16:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **155,332 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 16:16:53 | Rathnapura (Kalu Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:10:20 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-05-18 16:10:18 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:08:54 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:07:47 | Peradeniya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-18 16:07:32 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.030 |  |
| 2026-05-18 16:06:54 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:05:05 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-18 16:05:01 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-18 16:04:14 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:03:51 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:03:48 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-05-18 16:03:32 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-05-18 16:03:29 | Hanwella (Kelani Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-05-18 16:03:28 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-18 16:03:28 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-18 16:03:24 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.032 |  |
| 2026-05-18 16:03:11 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.264 |  |
| 2026-05-18 16:03:08 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.060 |  |
| 2026-05-18 16:03:03 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-05-18 16:03:00 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:02:45 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:02:38 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:02:30 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:02:27 | Putupaula (Kalu Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:02:23 | Glencourse (Kelani Ganga) | 10.09 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-18 16:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.40 | 🟡 Alert | -0.062 |  |
| 2026-05-18 16:02:17 | Ellagawa (Kalu Ganga) | 5.94 | 🟢 Normal | -0.060 |  |
| 2026-05-18 16:01:58 | Thanthirimale (Malwathu Oya) | 2.90 | 🟢 Normal | -0.041 |  |
| 2026-05-18 16:01:54 | Galgamuwa (Mee Oya) | 1.75 | 🟢 Normal | -0.052 |  |
| 2026-05-18 16:01:53 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | -0.021 |  |
| 2026-05-18 16:01:20 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-18 16:01:16 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.011 |  |
| 2026-05-18 16:01:12 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:01:11 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:00:48 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:00:30 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:00:21 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:00:19 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:00:18 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:00:17 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 16:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.40 | 🟡 Alert | -0.062 |  |
| 2026-05-18 16:07:47 | Peradeniya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-18 16:02:23 | Glencourse (Kelani Ganga) | 10.09 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-18 16:01:20 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-18 16:03:28 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-18 16:05:01 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-18 16:05:05 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-18 16:03:28 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-18 16:01:11 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:00:30 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:03:00 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:04:14 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:10:18 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:02:38 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:08:54 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:01:12 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:00:21 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:02:30 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:02:27 | Putupaula (Kalu Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:00:48 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:16:53 | Rathnapura (Kalu Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:06:54 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-18 15:26:24 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:03:51 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:02:45 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:10:20 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-05-18 16:03:29 | Hanwella (Kelani Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-05-18 16:03:48 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-05-18 16:03:32 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-05-18 16:03:03 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-05-18 16:01:16 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.011 |  |
| 2026-05-18 16:01:53 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | -0.021 |  |
| 2026-05-18 16:07:32 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.030 |  |
| 2026-05-18 16:03:24 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.032 |  |
| 2026-05-18 16:01:58 | Thanthirimale (Malwathu Oya) | 2.90 | 🟢 Normal | -0.041 |  |
| 2026-05-18 16:01:54 | Galgamuwa (Mee Oya) | 1.75 | 🟢 Normal | -0.052 |  |
| 2026-05-18 16:02:17 | Ellagawa (Kalu Ganga) | 5.94 | 🟢 Normal | -0.060 |  |
| 2026-05-18 16:03:08 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.060 |  |
| 2026-05-18 16:03:11 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.264 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)