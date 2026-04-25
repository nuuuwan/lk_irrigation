# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_22:28:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **135,016 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 22:28:00 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:12:55 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:11:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-04-25 22:11:27 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.073 |  |
| 2026-04-25 22:11:09 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-25 22:08:35 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | -0.019 |  |
| 2026-04-25 22:08:25 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-25 22:07:53 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:07:39 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:07:31 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.019 |  |
| 2026-04-25 22:07:00 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.009 |  |
| 2026-04-25 22:06:39 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:06:26 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:05:40 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-04-25 22:05:23 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 22:05:11 | Katharagama (Menik Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:04:49 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:04:29 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | -0.019 |  |
| 2026-04-25 22:04:13 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:03:37 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:03:31 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:03:18 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:03:02 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-04-25 22:02:55 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-04-25 22:02:51 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:02:50 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-04-25 22:02:38 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.081 |  |
| 2026-04-25 22:02:36 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-04-25 22:02:34 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.032 |  |
| 2026-04-25 22:02:13 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-04-25 22:02:03 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:01:40 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:01:30 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:01:24 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:00:41 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 22:11:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-04-25 22:11:09 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-25 22:08:25 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-25 22:05:23 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 22:04:49 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:01:30 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:03:37 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:01:59 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:06:39 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:12:55 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:28:00 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-25 21:06:01 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:02:03 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:00:41 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:02:51 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:03:31 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:05:11 | Katharagama (Menik Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:04:13 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:07:39 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:07:53 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:06:26 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:03:18 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 22:07:00 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.009 |  |
| 2026-04-25 22:02:36 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-04-25 22:05:40 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-04-25 22:03:02 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-04-25 22:02:13 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-04-25 22:02:55 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-04-25 22:07:31 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.019 |  |
| 2026-04-25 22:04:29 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | -0.019 |  |
| 2026-04-25 22:08:35 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | -0.019 |  |
| 2026-04-25 22:02:50 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-04-25 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.020 |  |
| 2026-04-25 18:01:09 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-04-25 21:03:53 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.029 |  |
| 2026-04-25 22:02:34 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.032 |  |
| 2026-04-25 18:00:50 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.050 |  |
| 2026-04-25 22:11:27 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.073 |  |
| 2026-04-25 22:02:38 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)