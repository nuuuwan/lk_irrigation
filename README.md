# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--20_17:19:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **184,663 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 17:19:15 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:17:59 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-20 17:10:34 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.018 |  |
| 2026-06-20 17:09:34 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.009 |  |
| 2026-06-20 17:08:59 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:08:33 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.009 |  |
| 2026-06-20 17:07:50 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-20 17:07:35 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:07:26 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-20 17:06:46 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:06:28 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-06-20 17:06:18 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-06-20 17:06:02 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:05:47 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:05:21 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:04:15 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-06-20 17:04:13 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-06-20 17:03:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.06 | 🟢 Normal | -0.049 |  |
| 2026-06-20 17:03:38 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:03:24 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-20 17:03:22 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | -0.020 |  |
| 2026-06-20 17:03:06 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-20 17:02:58 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-06-20 17:02:39 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:02:18 | Glencourse (Kelani Ganga) | 9.89 | 🟢 Normal | -0.084 |  |
| 2026-06-20 17:02:12 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:02:12 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-20 17:01:52 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:01:45 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:01:35 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:01:15 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:01:15 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:01:14 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:01:10 | Ellagawa (Kalu Ganga) | 5.33 | 🟢 Normal | -0.021 |  |
| 2026-06-20 17:01:09 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:00:51 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 17:04:13 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-06-20 17:03:24 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-20 17:17:59 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-20 17:07:50 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-20 17:07:26 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-20 17:02:12 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-20 17:03:06 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-20 17:03:38 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:00:51 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:01:15 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:19:15 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:01:52 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:01:09 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:07:35 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-06-20 16:03:56 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:08:59 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:02:12 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:01:35 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:06:46 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:05:21 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:06:02 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:05:47 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:01:15 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:02:39 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:01:45 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:01:14 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 17:08:33 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.009 |  |
| 2026-06-20 17:09:34 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.009 |  |
| 2026-06-20 17:04:15 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-06-20 17:06:28 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-06-20 17:02:58 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-06-20 17:06:18 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-06-20 16:01:55 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.011 |  |
| 2026-06-20 17:10:34 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.018 |  |
| 2026-06-20 17:03:22 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | -0.020 |  |
| 2026-06-20 17:01:10 | Ellagawa (Kalu Ganga) | 5.33 | 🟢 Normal | -0.021 |  |
| 2026-06-20 17:03:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.06 | 🟢 Normal | -0.049 |  |
| 2026-06-20 17:02:18 | Glencourse (Kelani Ganga) | 9.89 | 🟢 Normal | -0.084 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)