# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--15_07:06:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **179,820 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-15 07:06:17 | Magura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.019 |  |
| 2026-06-15 07:06:12 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-06-15 07:06:00 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-06-15 07:05:17 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-15 07:05:07 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | -0.029 |  |
| 2026-06-15 07:04:27 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.048 |  |
| 2026-06-15 07:04:27 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-15 07:04:19 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-06-15 07:04:11 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.048 |  |
| 2026-06-15 07:04:10 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-15 07:04:06 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-06-15 07:03:45 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-15 07:03:44 | Panadugama (Nilwala Ganga) | 3.23 | 🟢 Normal | -0.094 |  |
| 2026-06-15 07:03:34 | Hanwella (Kelani Ganga) | 2.77 | 🟢 Normal | -0.039 |  |
| 2026-06-15 07:03:17 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-06-15 07:03:12 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-15 07:03:04 | Ellagawa (Kalu Ganga) | 6.73 | 🟢 Normal | -0.091 |  |
| 2026-06-15 07:02:54 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | -0.020 |  |
| 2026-06-15 07:02:41 | Galgamuwa (Mee Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-15 07:02:38 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.020 |  |
| 2026-06-15 07:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.35 | 🟡 Alert | -0.187 |  |
| 2026-06-15 07:02:07 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-15 07:01:57 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-06-15 07:01:39 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-06-15 07:01:26 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | -0.011 |  |
| 2026-06-15 07:01:21 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.040 |  |
| 2026-06-15 07:01:00 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-06-15 07:00:56 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-15 07:00:54 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-06-15 07:00:44 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | -0.090 |  |
| 2026-06-15 06:31:00 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-06-15 06:25:11 | Galgamuwa (Mee Oya) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-15 07:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.35 | 🟡 Alert | -0.187 |  |
| 2026-06-15 05:01:12 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 54.000 | 🔺 Rising |
| 2026-06-15 07:06:12 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-06-15 07:03:12 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-15 07:00:56 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-15 07:01:39 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-06-15 06:02:57 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-15 07:02:41 | Galgamuwa (Mee Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-15 07:03:45 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-15 07:04:10 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-15 06:03:02 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-15 07:01:00 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-06-15 07:04:19 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-06-15 07:05:17 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-15 06:03:24 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-15 07:02:07 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-15 07:06:00 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-06-15 07:03:17 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-06-15 07:04:06 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-06-15 07:00:54 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-06-15 07:01:57 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-06-15 07:04:27 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-15 07:01:26 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | -0.011 |  |
| 2026-06-15 06:04:20 | Baddegama (Gin Ganga) | 2.26 | 🟢 Normal | -0.011 |  |
| 2026-06-15 07:06:17 | Magura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.019 |  |
| 2026-06-15 07:02:54 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | -0.020 |  |
| 2026-06-15 07:02:38 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.020 |  |
| 2026-06-15 07:05:07 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | -0.029 |  |
| 2026-06-15 06:04:48 | Glencourse (Kelani Ganga) | 10.73 | 🟢 Normal | -0.030 |  |
| 2026-06-15 06:00:53 | Rathnapura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.037 |  |
| 2026-06-15 07:03:34 | Hanwella (Kelani Ganga) | 2.77 | 🟢 Normal | -0.039 |  |
| 2026-06-15 07:01:21 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.040 |  |
| 2026-06-15 07:04:27 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.048 |  |
| 2026-06-15 07:04:11 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.048 |  |
| 2026-06-15 06:09:01 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.061 |  |
| 2026-06-15 07:00:44 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | -0.090 |  |
| 2026-06-15 07:03:04 | Ellagawa (Kalu Ganga) | 6.73 | 🟢 Normal | -0.091 |  |
| 2026-06-15 07:03:44 | Panadugama (Nilwala Ganga) | 3.23 | 🟢 Normal | -0.094 |  |
| 2026-06-15 06:03:02 | Putupaula (Kalu Ganga) | 2.30 | 🟢 Normal | -0.099 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)