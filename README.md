# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--14_09:12:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **179,013 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 09:12:46 | Panadugama (Nilwala Ganga) | 3.96 | 🟢 Normal | -0.018 |  |
| 2026-06-14 09:11:48 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-06-14 09:11:23 | Magura (Kalu Ganga) | 2.92 | 🟢 Normal | -0.047 |  |
| 2026-06-14 09:11:15 | Putupaula (Kalu Ganga) | 2.64 | 🟢 Normal | -0.009 |  |
| 2026-06-14 09:11:00 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-06-14 09:08:11 | Glencourse (Kelani Ganga) | 11.33 | 🟢 Normal | -0.055 |  |
| 2026-06-14 09:07:45 | Badalgama (Maha Oya) | 3.17 | 🟢 Normal | -0.010 |  |
| 2026-06-14 09:07:35 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-14 09:07:33 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-14 09:07:07 | Baddegama (Gin Ganga) | 2.85 | 🟢 Normal | -0.029 |  |
| 2026-06-14 09:06:51 | Dunamale (Aththanagalu Oya) | 3.12 | 🟢 Normal | -0.019 |  |
| 2026-06-14 09:05:40 | Rathnapura (Kalu Ganga) | 3.67 | 🟢 Normal | -0.091 |  |
| 2026-06-14 09:05:06 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-14 09:05:01 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-14 09:04:04 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-14 09:03:55 | Galgamuwa (Mee Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-14 09:03:38 | Hanwella (Kelani Ganga) | 3.63 | 🟢 Normal | -0.030 |  |
| 2026-06-14 09:03:26 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-14 09:03:18 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-06-14 09:03:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.38 | 🟡 Alert | -0.021 |  |
| 2026-06-14 09:03:08 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.059 |  |
| 2026-06-14 09:03:06 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-14 09:03:03 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-14 09:02:57 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-14 09:02:54 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-14 09:02:49 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-14 09:02:40 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | -0.020 |  |
| 2026-06-14 09:02:21 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-14 09:02:20 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.012 |  |
| 2026-06-14 09:02:18 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-14 09:02:03 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.024 |  |
| 2026-06-14 09:02:01 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-06-14 09:01:54 | Ellagawa (Kalu Ganga) | 8.46 | 🟢 Normal | -0.040 |  |
| 2026-06-14 09:01:43 | Nawalapitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-06-14 09:01:36 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-14 09:01:04 | Thalgahagoda (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.109 |  |
| 2026-06-14 09:00:23 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-14 09:00:15 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-06-14 08:59:38 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 09:03:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.38 | 🟡 Alert | -0.021 |  |
| 2026-06-14 09:04:04 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-14 09:00:15 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-06-14 09:05:06 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-14 09:03:03 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-14 09:00:23 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-14 09:07:33 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-14 09:02:01 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-06-14 09:01:36 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-14 09:02:57 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-14 09:02:18 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-14 09:03:55 | Galgamuwa (Mee Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-14 09:03:26 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-14 09:03:06 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-14 09:02:54 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-14 09:05:01 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-14 09:02:49 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-14 09:07:35 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-14 08:13:18 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.008 |  |
| 2026-06-14 09:11:48 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-06-14 09:11:15 | Putupaula (Kalu Ganga) | 2.64 | 🟢 Normal | -0.009 |  |
| 2026-06-14 09:11:00 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-06-14 09:07:45 | Badalgama (Maha Oya) | 3.17 | 🟢 Normal | -0.010 |  |
| 2026-06-14 09:01:43 | Nawalapitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-06-14 09:03:18 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-06-14 09:02:20 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.012 |  |
| 2026-06-14 09:12:46 | Panadugama (Nilwala Ganga) | 3.96 | 🟢 Normal | -0.018 |  |
| 2026-06-14 09:06:51 | Dunamale (Aththanagalu Oya) | 3.12 | 🟢 Normal | -0.019 |  |
| 2026-06-14 09:02:40 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | -0.020 |  |
| 2026-06-14 08:59:38 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.021 |  |
| 2026-06-14 09:02:03 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.024 |  |
| 2026-06-14 09:07:07 | Baddegama (Gin Ganga) | 2.85 | 🟢 Normal | -0.029 |  |
| 2026-06-14 09:03:38 | Hanwella (Kelani Ganga) | 3.63 | 🟢 Normal | -0.030 |  |
| 2026-06-14 09:01:54 | Ellagawa (Kalu Ganga) | 8.46 | 🟢 Normal | -0.040 |  |
| 2026-06-14 09:11:23 | Magura (Kalu Ganga) | 2.92 | 🟢 Normal | -0.047 |  |
| 2026-06-14 09:08:11 | Glencourse (Kelani Ganga) | 11.33 | 🟢 Normal | -0.055 |  |
| 2026-06-14 09:03:08 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.059 |  |
| 2026-06-14 09:05:40 | Rathnapura (Kalu Ganga) | 3.67 | 🟢 Normal | -0.091 |  |
| 2026-06-14 09:01:04 | Thalgahagoda (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.109 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)