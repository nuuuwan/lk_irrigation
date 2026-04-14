# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_07:19:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **124,626 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 07:19:52 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 07:13:57 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.041 |  |
| 2026-04-14 07:13:49 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-14 07:10:41 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-14 07:09:14 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-14 07:07:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | -0.174 |  |
| 2026-04-14 07:07:35 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-04-14 07:06:39 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-14 07:06:26 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-14 07:06:11 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-04-14 07:06:03 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.009 |  |
| 2026-04-14 07:05:15 | Thanamalwila (Kirindi Oya) | 1.64 | 🟢 Normal | -0.021 |  |
| 2026-04-14 07:05:01 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-14 07:04:46 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.000 |  |
| 2026-04-14 07:04:39 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-14 07:04:30 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-04-14 07:04:10 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-14 07:03:10 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-14 07:02:52 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-14 07:02:51 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-14 07:02:47 | Thanthirimale (Malwathu Oya) | 4.15 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-04-14 07:02:45 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-14 07:02:43 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.060 |  |
| 2026-04-14 07:02:26 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-14 07:01:58 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | -0.020 |  |
| 2026-04-14 07:01:53 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-14 07:01:51 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.060 |  |
| 2026-04-14 07:01:44 | Kuda Oya (Kirindi Oya) | 1.82 | 🟢 Normal | -0.143 |  |
| 2026-04-14 07:01:36 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-04-14 07:01:31 | Ellagawa (Kalu Ganga) | 4.73 | 🟢 Normal | -0.063 |  |
| 2026-04-14 07:01:22 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 07:01:11 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.320 |  |
| 2026-04-14 07:01:09 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.011 |  |
| 2026-04-14 07:00:39 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-04-14 07:00:29 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.036 |  |
| 2026-04-14 07:00:12 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-14 07:00:10 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.043 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 07:02:47 | Thanthirimale (Malwathu Oya) | 4.15 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-04-14 07:02:51 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-14 06:00:45 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-14 07:03:10 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-14 07:04:39 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-14 07:05:01 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-14 07:01:53 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-14 07:19:52 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 07:09:14 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-14 07:01:22 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 07:00:12 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-14 07:07:35 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-04-14 07:04:10 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-14 07:04:46 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.000 |  |
| 2026-04-14 07:02:26 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-14 07:06:26 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-14 07:06:39 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-14 07:13:49 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-14 07:06:03 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.009 |  |
| 2026-04-14 07:02:52 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-14 07:06:11 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-04-14 07:00:39 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-04-14 07:02:45 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-14 07:01:09 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.011 |  |
| 2026-04-14 06:05:36 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-04-14 07:01:36 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-04-14 07:04:30 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-04-14 07:01:58 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | -0.020 |  |
| 2026-04-14 07:05:15 | Thanamalwila (Kirindi Oya) | 1.64 | 🟢 Normal | -0.021 |  |
| 2026-04-14 07:00:29 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.036 |  |
| 2026-04-14 07:13:57 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.041 |  |
| 2026-04-14 07:00:10 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.043 |  |
| 2026-04-14 07:01:51 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.060 |  |
| 2026-04-14 07:02:43 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.060 |  |
| 2026-04-14 07:01:31 | Ellagawa (Kalu Ganga) | 4.73 | 🟢 Normal | -0.063 |  |
| 2026-04-14 06:01:41 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.080 |  |
| 2026-04-14 07:01:44 | Kuda Oya (Kirindi Oya) | 1.82 | 🟢 Normal | -0.143 |  |
| 2026-04-14 07:07:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | -0.174 |  |
| 2026-04-14 07:01:11 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.320 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)