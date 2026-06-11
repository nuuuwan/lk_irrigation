# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--11_07:01:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **176,219 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 07:01:41 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.021 |  |
| 2026-06-11 07:01:30 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.059 |  |
| 2026-06-11 07:01:28 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 07:01:27 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-11 07:00:53 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 07:00:27 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-11 07:00:17 | Nagalagam Street (Kelani Ganga) | 0.53 | 🟢 Normal | -0.018 |  |
| 2026-06-11 07:00:09 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-11 07:00:08 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-11 06:59:53 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-11 06:42:25 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | -0.002 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 06:06:24 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-06-11 06:01:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.44 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-06-11 06:04:06 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-11 06:08:22 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-11 06:04:41 | Deraniyagala (Kelani Ganga) | 1.25 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-11 06:00:10 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-11 06:06:25 | Hanwella (Kelani Ganga) | 2.54 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-11 07:00:53 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 06:08:07 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-11 06:04:38 | Ellagawa (Kalu Ganga) | 5.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-11 06:01:02 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-11 06:01:23 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-11 06:03:19 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 07:01:28 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 06:08:36 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-11 06:05:38 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-06-11 07:00:09 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-11 06:06:02 | Moragaswewa (Deduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-11 07:00:27 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-11 06:06:04 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 06:01:46 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-11 06:00:07 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-11 06:05:42 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-11 06:06:13 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-06-11 06:00:42 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:06:20 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.000 |  |
| 2026-06-11 06:01:58 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-10 18:23:24 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-11 07:00:08 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-11 06:01:22 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-11 07:01:27 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-11 06:42:25 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | -0.002 |  |
| 2026-06-11 06:01:18 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-06-11 06:02:41 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-06-11 06:00:48 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.012 |  |
| 2026-06-11 07:00:17 | Nagalagam Street (Kelani Ganga) | 0.53 | 🟢 Normal | -0.018 |  |
| 2026-06-11 07:01:41 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.021 |  |
| 2026-06-11 06:01:53 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.051 |  |
| 2026-06-11 07:01:30 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)