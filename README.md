# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--13_09:17:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **178,119 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 09:17:35 | Pitabeddara (Nilwala Ganga) | 1.61 | 🟢 Normal | -0.059 |  |
| 2026-06-13 09:14:26 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-13 09:08:26 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-13 09:08:21 | Galgamuwa (Mee Oya) | 1.62 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-06-13 09:08:15 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | -0.058 |  |
| 2026-06-13 09:07:54 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.019 |  |
| 2026-06-13 09:07:46 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.019 |  |
| 2026-06-13 09:07:29 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-06-13 09:07:28 | Baddegama (Gin Ganga) | 3.17 | 🟢 Normal | 0.000 |  |
| 2026-06-13 09:07:23 | Badalgama (Maha Oya) | 3.48 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-13 09:06:52 | Holombuwa (Kelani Ganga) | 1.67 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-06-13 09:05:59 | Magura (Kalu Ganga) | 4.29 | 🟡 Alert | -0.062 |  |
| 2026-06-13 09:05:45 | Panadugama (Nilwala Ganga) | 4.68 | 🟢 Normal | -0.060 |  |
| 2026-06-13 09:05:29 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.076 |  |
| 2026-06-13 09:05:05 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-06-13 09:04:30 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-06-13 09:04:29 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.030 |  |
| 2026-06-13 09:04:12 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-06-13 09:04:00 | Hanwella (Kelani Ganga) | 4.02 | 🟢 Normal | -0.040 |  |
| 2026-06-13 09:03:49 | Giriulla (Maha Oya) | 2.49 | 🟢 Normal | -0.021 |  |
| 2026-06-13 09:03:46 | Putupaula (Kalu Ganga) | 2.41 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-13 09:03:39 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.144 |  |
| 2026-06-13 09:03:27 | Moragaswewa (Deduru Oya) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-13 09:03:25 | Rathnapura (Kalu Ganga) | 5.72 | 🟡 Alert | -0.102 |  |
| 2026-06-13 09:03:16 | Deraniyagala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-06-13 09:03:14 | Thawalama (Gin Ganga) | 2.97 | 🟢 Normal | -0.105 |  |
| 2026-06-13 09:03:09 | Glencourse (Kelani Ganga) | 11.84 | 🟢 Normal | 0.000 |  |
| 2026-06-13 09:03:08 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-06-13 09:02:54 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.069 |  |
| 2026-06-13 09:02:46 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-13 09:02:31 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-13 09:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.40 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-06-13 09:02:15 | Nawalapitiya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.059 |  |
| 2026-06-13 09:02:13 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-06-13 09:01:52 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-13 09:01:48 | Ellagawa (Kalu Ganga) | 8.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 09:01:35 | Dunamale (Aththanagalu Oya) | 3.30 | 🟡 Alert | 0.023 | 🔺 Rising |
| 2026-06-13 09:00:38 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-13 09:00:10 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 09:01:35 | Dunamale (Aththanagalu Oya) | 3.30 | 🟡 Alert | 0.023 | 🔺 Rising |
| 2026-06-13 09:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.40 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-06-13 09:05:59 | Magura (Kalu Ganga) | 4.29 | 🟡 Alert | -0.062 |  |
| 2026-06-13 09:03:25 | Rathnapura (Kalu Ganga) | 5.72 | 🟡 Alert | -0.102 |  |
| 2026-06-13 09:03:08 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-06-13 09:06:52 | Holombuwa (Kelani Ganga) | 1.67 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-06-13 09:07:23 | Badalgama (Maha Oya) | 3.48 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-13 09:08:21 | Galgamuwa (Mee Oya) | 1.62 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-06-13 09:00:38 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-13 09:03:27 | Moragaswewa (Deduru Oya) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-13 09:03:46 | Putupaula (Kalu Ganga) | 2.41 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-13 09:01:48 | Ellagawa (Kalu Ganga) | 8.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 09:02:31 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-13 09:01:52 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-13 09:14:26 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-13 09:07:28 | Baddegama (Gin Ganga) | 3.17 | 🟢 Normal | 0.000 |  |
| 2026-06-13 09:03:09 | Glencourse (Kelani Ganga) | 11.84 | 🟢 Normal | 0.000 |  |
| 2026-06-13 09:04:12 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-06-13 09:08:26 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-13 09:07:29 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-06-13 08:01:51 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-06-13 09:03:16 | Deraniyagala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-06-13 09:04:30 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-06-13 09:00:10 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-06-13 09:07:46 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.019 |  |
| 2026-06-13 09:07:54 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.019 |  |
| 2026-06-13 09:02:13 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-06-13 09:05:05 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-06-13 09:03:49 | Giriulla (Maha Oya) | 2.49 | 🟢 Normal | -0.021 |  |
| 2026-06-13 09:04:29 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.030 |  |
| 2026-06-13 09:04:00 | Hanwella (Kelani Ganga) | 4.02 | 🟢 Normal | -0.040 |  |
| 2026-06-13 09:08:15 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | -0.058 |  |
| 2026-06-13 09:17:35 | Pitabeddara (Nilwala Ganga) | 1.61 | 🟢 Normal | -0.059 |  |
| 2026-06-13 09:02:15 | Nawalapitiya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.059 |  |
| 2026-06-13 09:05:45 | Panadugama (Nilwala Ganga) | 4.68 | 🟢 Normal | -0.060 |  |
| 2026-06-13 09:02:54 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.069 |  |
| 2026-06-13 09:05:29 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.076 |  |
| 2026-06-13 09:03:14 | Thawalama (Gin Ganga) | 2.97 | 🟢 Normal | -0.105 |  |
| 2026-06-13 09:03:39 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.144 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)