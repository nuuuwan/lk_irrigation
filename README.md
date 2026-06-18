# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--19_05:17:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **183,300 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 05:17:10 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | -0.024 |  |
| 2026-06-19 05:14:30 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-19 05:12:58 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-19 05:12:47 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-19 05:11:31 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.009 |  |
| 2026-06-19 05:09:19 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-06-19 05:08:47 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.034 |  |
| 2026-06-19 05:07:56 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.016 |  |
| 2026-06-19 05:07:56 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-19 05:07:55 | Panadugama (Nilwala Ganga) | 3.04 | 🟢 Normal | -0.048 |  |
| 2026-06-19 05:07:23 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-19 05:06:14 | Rathnapura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-06-19 05:05:30 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.012 |  |
| 2026-06-19 05:05:13 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-06-19 05:04:52 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-19 05:04:48 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.019 |  |
| 2026-06-19 05:04:43 | Dunamale (Aththanagalu Oya) | 2.69 | 🟢 Normal | -0.029 |  |
| 2026-06-19 05:04:41 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-19 05:04:39 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-19 05:04:29 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 05:04:23 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | -0.020 |  |
| 2026-06-19 05:04:04 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-06-19 05:04:00 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.058 |  |
| 2026-06-19 05:03:57 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 05:02:53 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-19 05:02:45 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-19 05:02:40 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-19 05:02:26 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-06-19 05:02:23 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.302 | 🔺 Rising |
| 2026-06-19 05:02:02 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | -0.013 |  |
| 2026-06-19 05:01:58 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-19 05:01:47 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-19 05:01:45 | Magura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.077 |  |
| 2026-06-19 05:01:30 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-19 05:01:03 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-19 05:00:49 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -36.000 |  |
| 2026-06-19 05:00:48 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | -36.000 |  |
| 2026-06-19 04:50:07 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-19 04:30:38 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.016 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 05:02:23 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.302 | 🔺 Rising |
| 2026-06-19 05:04:41 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-19 05:12:47 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-19 04:04:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.16 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-19 05:04:52 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-19 05:01:30 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-19 05:01:47 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-19 05:04:39 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-19 05:02:40 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-19 05:07:23 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-19 05:01:03 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-19 05:03:57 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 05:12:58 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:03:35 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-19 05:04:04 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-06-19 05:04:29 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 05:07:56 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-19 05:01:58 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-19 05:02:45 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:01:31 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-19 05:14:30 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-19 05:11:31 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.009 |  |
| 2026-06-19 05:05:13 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-06-19 05:09:19 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-06-19 05:02:26 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-06-19 05:05:30 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.012 |  |
| 2026-06-19 05:02:02 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | -0.013 |  |
| 2026-06-19 05:07:56 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.016 |  |
| 2026-06-19 05:04:48 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.019 |  |
| 2026-06-19 05:06:14 | Rathnapura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-06-19 05:04:23 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | -0.020 |  |
| 2026-06-19 05:17:10 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | -0.024 |  |
| 2026-06-19 05:04:43 | Dunamale (Aththanagalu Oya) | 2.69 | 🟢 Normal | -0.029 |  |
| 2026-06-19 05:08:47 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.034 |  |
| 2026-06-18 18:04:05 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.040 |  |
| 2026-06-19 05:07:55 | Panadugama (Nilwala Ganga) | 3.04 | 🟢 Normal | -0.048 |  |
| 2026-06-19 05:04:00 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.058 |  |
| 2026-06-19 05:01:45 | Magura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.077 |  |
| 2026-06-19 05:00:49 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)