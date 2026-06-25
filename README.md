# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--25_14:14:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **189,051 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 14:14:03 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-06-25 14:12:49 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:11:31 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-06-25 14:10:22 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.045 |  |
| 2026-06-25 14:09:16 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-06-25 14:08:54 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | -0.010 |  |
| 2026-06-25 14:08:17 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:07:14 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:06:47 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:06:42 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.009 |  |
| 2026-06-25 14:06:21 | Ellagawa (Kalu Ganga) | 5.43 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:05:48 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 14:05:15 | Putupaula (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:04:58 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.009 |  |
| 2026-06-25 14:04:21 | Hanwella (Kelani Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-06-25 14:03:56 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:03:55 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:03:44 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | -0.029 |  |
| 2026-06-25 14:03:11 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:03:11 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-06-25 14:03:06 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:03:05 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.010 |  |
| 2026-06-25 14:02:54 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:02:43 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-25 14:02:20 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:02:13 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:02:13 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-06-25 14:01:54 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:01:41 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-25 14:01:40 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:01:20 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:01:19 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:01:15 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:01:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.36 | 🟢 Normal | -0.061 |  |
| 2026-06-25 14:01:09 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:00:53 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.076 |  |
| 2026-06-25 14:00:46 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:00:00 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:59:26 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:39:35 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 14:11:31 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-06-25 14:01:41 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-25 14:02:43 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-25 14:05:48 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 14:03:11 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:07:14 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:06:47 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:02:13 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:02:20 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:01:19 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:12:49 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:01:54 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:03:55 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:06:21 | Ellagawa (Kalu Ganga) | 5.43 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:01:09 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:01:20 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:03:56 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:01:40 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:00:00 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:03:06 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:05:15 | Putupaula (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:08:17 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:02:54 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:01:15 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:00:46 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:06:42 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.009 |  |
| 2026-06-25 14:04:58 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.009 |  |
| 2026-06-25 14:08:54 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | -0.010 |  |
| 2026-06-25 14:04:21 | Hanwella (Kelani Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-06-25 14:02:13 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-06-25 14:03:05 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.010 |  |
| 2026-06-25 14:09:16 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-06-25 14:14:03 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-06-25 14:03:44 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | -0.029 |  |
| 2026-06-25 14:03:11 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-06-25 14:10:22 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.045 |  |
| 2026-06-25 14:01:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.36 | 🟢 Normal | -0.061 |  |
| 2026-06-25 14:00:53 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.076 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)